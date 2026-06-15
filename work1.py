while True:
    print("โปรแกรมคำนวณพื้นที่รูปสี่เหลี่ยมมุมฉาก")

    d = float(input("ใส่ความกว้าง"))
    l = float(input("ใส่ความยาว"))

    s = d * l
    print("พื้นที่คือ",s)
    
    ans = input("ต้องการใส่ทำต่อไหม(y/n)")
    if ans.lower() == "n":
        break
