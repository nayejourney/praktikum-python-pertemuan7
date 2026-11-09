"""
Program penghitungan diskon menggunakan prinsip Clean Code.
"""

BATAS_MINIMUM_DISKON = 100
DISKON_MEMBER = 0.05
DISKON_PROMO = 0.10
KODE_PROMO = "HEMAT"


def hitung_diskon(total_belanja, member, kode_promo):
    """Menghitung diskon berdasarkan status member dan kode promo."""

    if total_belanja <= BATAS_MINIMUM_DISKON:
        return 0

    if kode_promo == KODE_PROMO:
        return total_belanja * DISKON_PROMO

    if member:
        return total_belanja * DISKON_MEMBER

    return 0


def hitung_total_bayar(total_belanja, diskon):
    """Menghitung total pembayaran setelah diskon."""

    return total_belanja - diskon


def tampilkan_struk(total_belanja, diskon):
    """Menampilkan rincian pembayaran."""

    total_bayar = hitung_total_bayar(
        total_belanja,
        diskon
    )

    print("Total belanja :", total_belanja)
    print("Diskon        :", diskon)
    print("Total bayar   :", total_bayar)


def proses_pembelian(total_belanja, member, kode_promo):
    """Menjalankan proses pembelian."""

    if total_belanja < 0:
        raise ValueError("Total belanja tidak boleh negatif.")

    diskon = hitung_diskon(
        total_belanja,
        member,
        kode_promo
    )

    tampilkan_struk(total_belanja, diskon)


if __name__ == "__main__":

    proses_pembelian(
        total_belanja=250000,
        member=True,
        kode_promo="HEMAT"
    )