def calculate_salary(hours_worked, hourly_rate):
    # ชั่วโมงการทำงานปกติ
    regular_hours = 160
    overtime_rate = 1.5  # อัตราค่าล่วงเวลา 1.5 เท่าของค่าปกติ

    if hours_worked <= regular_hours:
        # กรณีทำงานไม่เกิน 160 ชั่วโมง
        total_salary = hours_worked * hourly_rate
    else:
        # กรณีทำงานเกิน 160 ชั่วโมง
        overtime_hours = hours_worked - regular_hours
        total_salary = (regular_hours * hourly_rate) + (overtime_hours * hourly_rate * overtime_rate)
    
    return total_salary

# รับข้อมูลจากผู้ใช้
try:
    hours_worked = float(input("กรุณาใส่จำนวนชั่วโมงการทำงานในเดือน: "))
    hourly_rate = float(input("กรุณาใส่อัตราค่าแรงต่อชั่วโมง: "))
    
    if hours_worked >= 0 and hourly_rate > 0:
        # คำนวณเงินเดือน
        total_salary = calculate_salary(hours_worked, hourly_rate)
        print(f"เงินเดือนรวมของคุณคือ: {total_salary:.2f} บาท")
    else:
        print("กรุณาใส่ค่าชั่วโมงและค่าแรงที่เป็นบวกเท่านั้น")
except ValueError:
    print("กรุณาใส่ตัวเลขที่ถูกต้อง")