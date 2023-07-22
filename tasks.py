from invoke import task

BEST_MODEL = "s3://...//model.pth"
S3_CSV_PATH = "s3://.../data.csv"
DEFAULT_EPOCHS = 5
DEFAULT_BATCH_SIZE = 32
DEFAULT_LEARNING_RATE = 1e-5


@task
def download_best_model(c, aws_path=BEST_MODEL):
    c.run(f"aws s3 cp {aws_path} models/")


@task
def prepare_data_for_pipeline(c, s3_csv_path=S3_CSV_PATH):
    c.run(f"aws s3 cp {s3_csv_path} data/raw_data.csv")


@task
def pipeline(c, epochs=DEFAULT_EPOCHS, batch_size=DEFAULT_BATCH_SIZE, learning_rate=DEFAULT_LEARNING_RATE):
    prepare_data_for_pipeline()
    c.run(f"python preproces.py")
    c.run(f"python train.py --epochs {epochs} --batch-size {batch_size} --learning-rate {learning_rate}")
