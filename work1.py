while True:
    print("เลือกการคำนวณพื้นที่")
    print("1.สี่เหลี่ยมมุมฉาก")
    print("2.สามเหลี่ยม")
    choice = input("เลือก(1หรือ2):")
    if choice == "1":
        print("โปรแกรมคำนวณพื้นที่รูปสี่เหลี่ยมมุมฉาก")

        d = float(input("ใส่ความกว้าง"))
        l = float(input("ใส่ความยาว"))

        s = d * l
        print("พื้นที่คือ",s)
    
    elif choice == "2":
        print("โปรแกรมหาพื้นที่รูปสามเหลี่ยม")
        b = float(input("ใส่ฐาน"))
        h = float(input("ใส่ความสูง"))

        a = 0.5 * b * h
        print("พื้นที่คือ",a)
    
    
    ans = input("ต้องการใส่ทำต่อไหม(y/n)")
    if ans.lower() == "n":
        break
