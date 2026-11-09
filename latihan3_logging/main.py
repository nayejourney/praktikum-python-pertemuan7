import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path


def atur_logging():

    logger = logging.getLogger("Aplikasi")
    logger.setLevel(logging.DEBUG)
    logger.handlers.clear()
    logger.propagate = False

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    file_handler = RotatingFileHandler(
        Path(__file__).with_name("app.log"),
        maxBytes=1024 * 1024,
        backupCount=3,
        encoding="utf-8"
    )

    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.WARNING)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


def main():

    logger = atur_logging()

    logger.debug("Aplikasi dimulai.")
    logger.info("Data berhasil dimuat.")
    logger.warning("Stok buku mulai menipis.")
    logger.error("Peminjaman gagal.")
    logger.critical("Terjadi kesalahan kritis.")

    print("Logging selesai. Periksa file app.log.")


if __name__ == "__main__":
    main()