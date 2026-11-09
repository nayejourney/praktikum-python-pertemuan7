def hitung_ipk(data_nilai):

    if not data_nilai:
        raise ValueError("Data nilai tidak boleh kosong.")

    total_mutu = 0
    total_sks = 0

    for nilai, sks in data_nilai:

        if nilai < 0 or nilai > 4:
            raise ValueError("Nilai harus 0 sampai 4.")

        if sks <= 0:
            raise ValueError("SKS harus lebih dari 0.")

        total_mutu += nilai * sks
        total_sks += sks

    return round(total_mutu / total_sks, 2)


def validasi_nim(nim):

    return len(nim) == 10 and nim.isdigit()


def konversi_nilai_huruf(nilai):

    if nilai < 0 or nilai > 100:
        raise ValueError("Nilai harus 0 sampai 100.")

    if nilai >= 85:
        return "A"
    elif nilai >= 80:
        return "B+"
    elif nilai >= 75:
        return "B"
    elif nilai >= 70:
        return "C+"
    elif nilai >= 60:
        return "C"
    elif nilai >= 50:
        return "D"
    else:
        return "E"


if __name__ == "__main__":

    print("IPK:", hitung_ipk([(4.0, 3), (3.5, 2)]))
    print("NIM:", validasi_nim("2026000001"))
    print("Nilai:", konversi_nilai_huruf(87))