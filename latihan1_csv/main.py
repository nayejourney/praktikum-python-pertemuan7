import csv
from pathlib import Path


def baca_data_mahasiswa():
    file_path = Path(__file__).with_name("mahasiswa.csv")
    file_csv = None
    data_mahasiswa = []

    try:
        file_csv = open(
            file_path,
            mode="r",
            newline="",
            encoding="utf-8"
        )

        reader = csv.DictReader(file_csv)

        for baris in reader:
            nim = baris["nim"].strip()
            nama = baris["nama"].strip()
            umur = int(baris["umur"])

            if not nim or not nama or umur <= 0:
                raise ValueError("Data mahasiswa tidak valid.")

            data_mahasiswa.append({
                "nim": nim,
                "nama": nama,
                "umur": umur
            })

    except FileNotFoundError:
        print("File CSV tidak ditemukan.")

    except csv.Error as error:
        print("Kesalahan CSV:", error)

    except (ValueError, KeyError) as error:
        print("Data tidak valid:", error)

    else:
        print("Data berhasil dibaca!")
        print("Jumlah mahasiswa:", len(data_mahasiswa))

        for mahasiswa in data_mahasiswa:
            print(
                mahasiswa["nim"],
                mahasiswa["nama"],
                mahasiswa["umur"]
            )

    finally:
        if file_csv is not None:
            file_csv.close()
            print("File berhasil ditutup.")


if __name__ == "__main__":
    baca_data_mahasiswa()