"""
Handles outputting the model predictions
"""
import numpy as np

from .handler import PredictionsHandler


class WritePredictionsHandler(PredictionsHandler):
    """
    Collects batches of model predictions and writes all of them
    to file at the end.

    Parameters
    ----------
    features : list(str)
        List of sequence-level features, in the same order that the
        model will return its predictions.
    columns_for_ids : list(str)
        Columns in the file that help to identify the input sequence to
        which the features data corresponds.
    output_path_prefix : str
        Path to the file to which Selene will write the absolute difference
        scores. The path may contain a filename prefix. Selene will append
        `predictions` to the end of the prefix.
    output_format : {'tsv', 'hdf5'}
        Specify the desired output format. TSV can be specified if you
        would like the final file to be easily perused. However, saving
        to a TSV file is much slower than saving to an HDF5 file.
    output_size : int, optional
        The total number of rows in the output. Must be specified when
        the output_format is hdf5.
    write_mem_limit : int, optional
        Default is 1500. Specify the amount of memory you can allocate to
        storing model predictions/scores for this particular handler, in MB.
        Handler will write to file whenever this memory limit is reached.
    write_labels : bool, optional
        Default is True. If you initialize multiple write handlers for the
        same set of inputs with output format `hdf5`, set `write_label` to
        False on all handlers except 1 so that only 1 handler writes the
        row labels to an output file.

    Attributes
    ----------
    needs_base_pred : bool
        Whether the handler needs the base (reference) prediction as input
        to compute the final output

    """

    def __init__(self,
                 features,
                 columns_for_ids,
                 output_path_prefix,
                 mult_predictions,
                 save_mult_pred,
                 output_format,
                 output_size=None,
                 write_mem_limit=1500,
                 write_labels=True):
        """
        Constructs a new `WritePredictionsHandler` object.
        """
        super(WritePredictionsHandler, self).__init__(
            features,
            columns_for_ids,
            output_path_prefix,
            mult_predictions,
            save_mult_pred,
            output_format,
            output_size=output_size,
            write_mem_limit=write_mem_limit,
            write_labels=write_labels)

        self.needs_base_pred = False
        self._results = []
        self._allResults = []
        self._samples = []

        self._features = features
        self._columns_for_ids = columns_for_ids
        self._output_path_prefix = output_path_prefix
        self._mult_predictions = mult_predictions
        self._save_mult_pred = save_mult_pred
        self._output_format = output_format
        self._write_mem_limit = write_mem_limit
        self._write_labels = write_labels

        # self._create_write_handler("predictions")
        if self._save_mult_pred:
            self._create_mult_write_handler("predictions", self._mult_predictions)
            self._create_write_handler("predictions")
        else:
            self._create_write_handler("predictions")

    def handle_batch_predictions(self,
                                 batch_predictions,
                                 batch_ids):
        """
        Handles the predictions for a batch of sequences.

        Parameters
        ----------
        batch_predictions : arraylike
            The predictions for a batch of sequences. This should have
            dimensions of :math:`B \\times N` (where :math:`B` is the
            size of the mini-batch and :math:`N` is the number of
            features).
        batch_ids : list(arraylike)
            Batch of sequence identifiers. Each element is `arraylike`
            because it may contain more than one column (written to
            file) that together make up a unique identifier for a
            sequence.
        """
        self._results.append(batch_predictions)
        self._samples.append(batch_ids)
        if self._reached_mem_limit():
            self.write_to_file()


    def handle_batch_mult_predictions(self,
                                 batch_predictions,
                                 batch_ids):

        if len(batch_predictions.shape) == 3:
            self._allResults.append(batch_predictions)
            self._results.append(np.mean(batch_predictions, axis=0))
            self._samples.append(batch_ids)
        if self._reached_mem_limit():
            self.write_to_file()

    def write_to_file(self):
        """
        Writes the stored scores to a file.

        """
        if self._save_mult_pred and self._mult_predictions>1:
            super().write_to_mult_files()
            # super().write_to_file()
        else:
            super().write_to_file()
