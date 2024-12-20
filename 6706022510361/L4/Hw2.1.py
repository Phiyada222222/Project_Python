def calculate_grade(score):
    if score >= 80:
        return "A"
    elif score >= 75:
        return "B+"
    elif score >= 70:
        return "B"
    elif score >= 65:
        return "C+"
    elif score >= 60:
        return "C"
    elif score >= 55:
        return "D+"
    elif score >= 50:
        return "D"
    else:
        return "F"

# รับคะแนนจากผู้ใช้
try:
    score = float(input("กรุณาใส่คะแนน (0-100): "))
    if 0 <= score <= 100:
        grade = calculate_grade(score)
        print(f"คะแนนของคุณคือ {score} ได้เกรด {grade}")
    else:
        print("กรุณาใส่คะแนนในช่วง 0-100")
except ValueError:
    print("กรุณาใส่ตัวเลขที่ถูกต้อง")