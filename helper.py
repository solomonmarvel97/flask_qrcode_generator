import qrcode
import uuid0

# data = name, employee id
def generate_id():
    return str(uuid0.generate())

def generate_qr_code(data: dict) -> str:
    "This function creates and save our qrcode information"
    unid = generate_id()
    img = qrcode.make(str({"id": unid, "employee_id": data["employee_id"]}))
    filename = "{}_{}.png".format(unid, data["name"]) 
    img.save(filename)

    # save user information to the db

    return filename
