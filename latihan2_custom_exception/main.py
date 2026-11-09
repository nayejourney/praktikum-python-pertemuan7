class PerpustakaanError(Exception):
    pass


class BukuNotFoundError(PerpustakaanError):
    pass


class BukuTidakTersediaError(PerpustakaanError):
    pass


class AnggotaNotFoundError(PerpustakaanError):
    pass


daftar_buku = {
    "B001": {
        "judul": "Belajar Python",
        "tersedia": True
    },
    "B002": {
        "judul": "Dasar Basis Data",
        "tersedia": False
    }
}


daftar_anggota = {
    "A001": "Naya",
    "A002": "Alya"
}


def pinjam_buku(kode_buku, id_anggota):

    if id_anggota not in daftar_anggota:
        raise AnggotaNotFoundError(
            "Anggota tidak ditemukan."
        )

    if kode_buku not in daftar_buku:
        raise BukuNotFoundError(
            "Buku tidak ditemukan."
        )

    buku = daftar_buku[kode_buku]

    if not buku["tersedia"]:
        raise BukuTidakTersediaError(
            "Buku sedang tidak tersedia."
        )

    buku["tersedia"] = False

    nama = daftar_anggota[id_anggota]

    return f"{nama} berhasil meminjam {buku['judul']}"


def main():

    kasus = [
        ("B001", "A001"),
        ("B999", "A001"),
        ("B002", "A001"),
        ("B001", "A999")
    ]

    for kode, anggota in kasus:

        try:
            hasil = pinjam_buku(kode, anggota)
            print(hasil)

        except PerpustakaanError as error:
            print("Gagal meminjam:", error)


if __name__ == "__main__":
    main()