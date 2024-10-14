import struct
import os
from collections import defaultdict

# Format ของ struct ในไฟล์ไบนารี
record_format = 'I20sf10sI'
record_size = struct.calcsize(record_format)
filename = 'data.bin'

# 1 ฟังก์ชันสำหรับเพิ่มข้อมูล
def add_record(record_id, name, price, product_type, quantity):
    with open(filename, 'ab') as file:
        name = name.ljust(20)[:20]
        product_type = product_type.ljust(10)[:10]
        record = struct.pack(record_format, record_id, name.encode('utf-8'), price, product_type.encode('utf-8'), quantity)
        file.write(record)

# 2 ฟังก์ชันสำหรับแสดงข้อมูลทั้งหมด
def display_records():
    # หัวตาราง
    print() # บรรทัดว่าง
    print("= "* 50 ) # เส้นคั่นตาราง
    print(f"{'ID':<10}{'Name':<35}{'Price':<15}{'Product Type':<20}{'Quantity':<10}")
    print("= "* 50 ) # เส้นคั่นตาราง
    
    with open(filename, 'rb') as file:
        while chunk := file.read(record_size):
            record = struct.unpack(record_format, chunk)
            # การจัดรูปแบบข้อมูลในแต่ละบรรทัด
            print(f"{record[0]:<10}{record[1].decode('utf-8').strip():<35}{record[2]:<17}{record[3].decode('utf-8').strip():<21}{record[4]:<10}")
    
    # ท้ายตาราง
    print("= "* 50 ,"\n") # เส้นคั่นตาราง


# 3 ฟังก์ชันสำหรับค้นหาข้อมูลตามรหัสสินค้า
def find_record_by_id(search_id):
    with open(filename, 'rb') as file:
        while chunk := file.read(record_size):
            record = struct.unpack(record_format, chunk)
            if record[0] == search_id:
                return record
    return None

# 4 ฟังก์ชันสำหรับอัปเดตข้อมูลสินค้า
def update_record(record_id, new_name=None, new_price=None, new_product_type=None, new_quantity=None):
    with open(filename, 'r+b') as file:
        chunk = file.read(record_size)
        while chunk :
            pos = file.tell() - record_size #Tell เอาไว้บอกตำเเหน่งที่อยู่ที่เราสนใจ
            record = struct.unpack(record_format, chunk)
            if record[0] == record_id:
                if new_name:
                    new_name = new_name.ljust(20)[:20]
                else:
                    new_name = record[1].decode()
                
                if new_product_type:
                    new_product_type = new_product_type.ljust(10)[:10]
                else:
                    new_product_type = record[3].decode()
                
                if new_price is None:
                    new_price = record[2]
                
                if new_quantity is None:
                    new_quantity = record[4]
                
                updated_record = struct.pack(record_format, record_id, new_name.encode(), new_price, 
                                             new_product_type.encode(), new_quantity)
                file.seek(pos)#seek คือการข้ามข้อมูล
                file.write(updated_record)
                break
            chunk = file.read(record_size)
# 5 ฟังก์ชันสำหรับลบข้อมูลสินค้า
def delete_record(record_id):
    temp_file = 'temp.bin'
    with open(filename, 'rb') as infile, open(temp_file, 'wb') as outfile:
        while chunk := infile.read(record_size):
            record = struct.unpack(record_format, chunk)
            if record[0] != record_id:
                outfile.write(chunk)
    os.replace(temp_file, filename)   

# 6 ฟังก์ชันสำหรับเขียนรายงาน
def generate_report_by_product_type():
    product_details = defaultdict(list)  # ใช้สำหรับเก็บรายละเอียดสินค้าต่อประเภท
    product_totals = defaultdict(float)  # ใช้สำหรับเก็บผลรวมของราคาสินค้าแต่ละประเภท
    product_quantities = defaultdict(int)  # ใช้สำหรับเก็บจำนวนสินค้ารวมต่อประเภท

    with open(filename, 'rb') as file:
        while chunk := file.read(record_size):
            record = struct.unpack(record_format, chunk)
            record_id = record[0]
            name = record[1].decode('utf-8').strip()
            price = record[2]
            product_type = record[3].decode('utf-8').strip()
            quantity = record[4]

            # เก็บรายละเอียดสินค้าในรูปแบบตาราง
            product_details[product_type].append(
                f"{record_id:<5}| {name:<30}| {price:>10.2f} | {quantity:>10} |"
            )

            # เพิ่มราคาสินค้าและจำนวนของประเภทนั้นๆ
            product_totals[product_type] += price * quantity
            product_quantities[product_type] += quantity

    # เริ่มสร้างรายงานแยกประเภทในรูปแบบตาราง
    report_content = "\n--------------------- รายงานแยกประเภทสินค้า ---------------------\n"
    report_content += f"จำนวนประเภทสินค้าทั้งหมด: {len(product_details)}\n" # ประเภทสินค้าที่มีในสต็อกทั้งหมด

    for product_type, items in product_details.items():
        report_content += "= " * 32 + "\n"# เส้นคั่นตาราง
        report_content += f"ประเภทสินค้า: {product_type}\n" # โชว์ประเภทสินค้า
        report_content += f"รายการสินค้าทั้งหมด: {len(items)}\n" # โชว์จำนวนสินค้าทั้งหมด
        report_content += "= " * 32 + "\n" # เส้นคั่นตาราง
        report_content += f"{'ID':<5}| {'Name':<30}| {'Price':>10} | {'Quantity':>10} |\n" # หัวข้อของข้อมูล
        report_content += " " * 63 + "\n"  # เส้นคั่นตาราง

        for item in items:
            report_content += f"{item}\n"

        report_content += "-" * 63 + "\n"  # เส้นคั่นตาราง
        # ยอดรวมจำนวนสินค้าและมูลค่าสินค้าของประเภทนั้น
        report_content += f"{'Total items:':<38} {product_quantities[product_type]:>10}\n"
        # มูลค่าสินค้าของสินค้าทั้้งหมดในประเภทนั้น
        report_content += f"{'Total value:':<38} {product_totals[product_type]:>10.2f}\n"
        report_content += " " * 63 + "\n"  # เส้นคั่นตาราง

    # บันทึกรายงานลงในไฟล์ report.txt
    with open('report.txt', 'w', encoding='utf-8') as report_file:
        report_file.write(report_content)
    print()
    print("\n""------- รายงานได้ถูกบันทึกลงในไฟล์ 'report.txt' เรียบร้อยแล้ว. ---------""\n")
    print()
# เมนูสำหรับเลือกฟังก์ชัน
def menu():
    while True:
        print("1. เพิ่มข้อมูล")
        print("2. แสดงข้อมูลทั้งหมด")
        print("3. ค้นหาข้อมูล")
        print("4. อัปเดตข้อมูล")
        print("5. ลบข้อมูล")
        print("6. สร้างรายงาน")
        print("7. ออกจากโปรแกรม")
        print()
        choice = int(input("เลือกฟังก์ชัน (1 - 7): "))

        if choice == 1:
            record_id = int(input("Enter ID(รหัสสินค้า): "))
            name = input("Enter Name(ชื่่อสินค้า): ")
            price = float(input("Enter Price(ราคาสินค้า): "))
            product_type = input("Enter Product Type(ประเภทสินค้า): ")
            quantity = int(input("Enter Quantity(จำนวนสินค้า): "))
            add_record(record_id, name, price, product_type, quantity)
        elif choice == 2:
            display_records()
        elif choice == 3:
            record_id = int(input("Enter ID to search (ค้นหาข้อมูล ID): "))
            record = find_record_by_id(record_id)
            if record:
                # แสดงหัวข้อของตาราง
                print()
                print("=" * 97)
                print(f"{'ID':<10}{'Name':<35}{'Price':<15}{'Product Type':<20}{'Quantity':<10}")
                print("=" * 97)
                
                # แสดงข้อมูลของ record ที่ค้นพบ
                print(f"{record[0]:<9}{record[1].decode().strip():<37}{record[2]:<17}{record[3].decode().strip():<20}{record[4]:<9}")
                print("-" * 97)
                print()
            else:
                print("ไม่พบข้อมูลที่บันทึก")
        elif choice == 4:
            print()
            record_id = int(input("Enter ID to update: "))
            name = input("Enter new name (เว้นว่างไว้เพื่อไม่ให้ มีการเปลี่ยนแปลง): ")
            price = input("Enter new price (เว้นว่างไว้เพื่อไม่ให้ มีการเปลี่ยนแปลง): ")
            product_type = input("Enter new product type (เว้นว่างไว้เพื่อไม่ให้ มีการเปลี่ยนแปลง): ")
            quantity = input("Enter new quantity (เว้นว่างไว้เพื่อไม่ให้ มีการเปลี่ยนแปลง): ")
            update_record(record_id, name or None, float(price) if price else None, product_type or None, int(quantity) if quantity else None)
            print()
        elif choice == 5:
            record_id = int(input("Enter ID to delete (เลือกเลข ID ที่ต้องการลบ): "))
            delete_record(record_id)
        elif choice == 6:
             generate_report_by_product_type()
        elif choice == 7:
            print()
            print("-------------------------------------------- จบโปรแกรม ----------------------------------------------------")
            print()
            break
        else:
            print("\n""ตัวเลือกไม่ถูกต้อง โปรดลองอีกครั้ง ให้เลือก(1 - 7)""\n")

# เริ่มโปรแกรม
menu()
