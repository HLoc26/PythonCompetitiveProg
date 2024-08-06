def calculate_electricity_bill(kw):
    if kw <= 50:
        return kw * 1.678
    elif kw <= 100:
        return 50 * 1.678 + (kw - 50) * 1.734
    elif kw <= 200:
        return 50 * 1.678 + 50 * 1.734 + (kw - 100) * 2.014
    elif kw <= 300:
        return 50 * 1.678 + 50 * 1.734 + 100 * 2.014 + (kw - 200) * 2.536
    elif kw <= 400:
        return 50 * 1.678 + 50 * 1.734 + 100 * 2.014 + 100 * 2.536 + (kw - 300) * 2.834
    else:
        return 50 * 1.678 + 50 * 1.734 + 100 * 2.014 + 100 * 2.536 + 100 * 2.834 + (kw - 400) * 2.927

# Nhập số KW từ người dùng
kw_used = float(input())

# Tính và in ra hóa đơn
bill = calculate_electricity_bill(kw_used)
print(f"{bill*1000:.0f}")