import sendgrid

sg = sendgrid.SendGridClient('userName', 'pass')

message = sendgrid.Mail()

#Email to a single recipient.  
message.add_to('example@email.com')

#Emails for various recipients via array. 
emails = ["example@email.com","exampleEmail@email.com"]
for email in emails: 
  message.add_to(email)

message.set_subject('Your subject here')
message.set_html('Body')
message.set_text('text here')
message.set_from('youremail@example.com')

#attachments  
message.add_attachment('filename.png','./fileLocation.png')

sg.send(message)
