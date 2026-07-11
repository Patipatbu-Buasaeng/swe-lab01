def calculate_grade(scores):
    # 1. ตรวจสอบว่า scores เป็น list หรือไม่ และมีข้อมูลหรือไม่ (ป้องกัน Bug หารด้วย 0)
    if not scores or not isinstance(scores, list):
        return "N/A", 0

    # 2. ใช้ sum() เพื่อความรวดเร็วและอ่านง่าย
    total = sum(scores)
    average = total / len(scores)

    # 3. การตัดเกรด (ตรรกะเดิมถูกต้องแล้ว)
    if average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"
        
    return grade, average

# การทดสอบกรณีปกติ
scores = [85, 92, 78, 88, 95]
grade, avg = calculate_grade(scores)
print(f"เกรด: {grade}, คะแนนเฉลี่ย: {avg}")

# การทดสอบกรณี List ว่าง (จุดที่เคยเป็น Bug)
empty_scores = []
grade, avg = calculate_grade(empty_scores)
print(f"กรณี List ว่าง -> เกรด: {grade}, คะแนนเฉลี่ย: {avg}")
print(calculate_grade([]))   # กรณีไม่มีคะแนนเลย
