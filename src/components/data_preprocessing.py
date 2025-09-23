from src.exception_handler import handle_exception
from src.logger import logging
from src.utils import binary_encoder, date_feature_extractor


def data_preprocessing(df):
    """
    Preprocess the DataFrame by dropping unnecessary columns.

    This method drops the 'Heart Attack Date' column from the DataFrame.

    Args:
        df (pd.DataFrame): The input DataFrame to preprocess.

    Returns:
        pd.DataFrame: The preprocessed DataFrame.
    """
    try:

        all_nan_cols = df.columns[df.isna().all()].tolist()
        df = df.drop(columns=all_nan_cols, axis=1)
        logging.info(f"Dropped all NaN columns: {all_nan_cols}")

        df = binary_encoder(df, target="Heart Attack Related to Vaccine")
        logging.info("Binary encoding done to create traget variable")

        date_feature_extractor(df, date_column="Heart Attack Date")
        date_feature_extractor(df, date_column="Vaccination Date")
        logging.info("Date feature extraction done")

        return df
    except Exception as e:
        raise handle_exception(e)
