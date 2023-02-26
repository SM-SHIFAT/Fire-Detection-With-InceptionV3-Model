import os
import smtplib
import imghdr
from email.message import EmailMessage

def sentMail():
    try:
        # EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
        # EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
        EMAIL_ADDRESS = 'fire.alert.ugv@gmail.com'
        EMAIL_PASSWORD = 'aughuzocnzidtdoy'

        contacts = ['sahriarnazmul272@gmail.com', 'mahfuzrahman129@gmail.com','minhazsharif209@gmail.com','moyeen5221@gmail.com']

        msg = EmailMessage()
        msg['Subject'] = 'Fire Alert! Check this details about the fire report.'
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = ', '.join(contacts)
        #msg['To'] = 'mahfuzrahman129@gmail.com'

        msg.set_content('This is an automated generated Email. Sent by The fire detection script. Please review the below image:')

        # msg.add_alternative("""\
        # <!DOCTYPE html>
        # <html>
        #     <body>
        #         <h1 style="color:SlateGray;">This is an HTML Email!</h1>
        #     </body>
        # </html>
        # """, subtype='html')
        source_dir = "./output"
        files = os.listdir(source_dir)

        for file in files:
            with open("./output/"+file, 'rb') as f:
                file_data = f.read()
                file_type = imghdr.what(f.name)
                file_name = f.name
            msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)





    except EOFError:
        print(EOFError)