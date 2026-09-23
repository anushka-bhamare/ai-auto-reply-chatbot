from openai import OpenAI
import os

client=OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)
command='''
[9:45 pm, 17/7/2026] Sakshi Kolekar Skn: Hi
[9:46 pm, 17/7/2026] Sakshi Kolekar Skn: Call kela hotas tu kay mhantey bol na
[9:47 pm, 17/7/2026] Anushka Bhamare: Arre admission form var konachi sign ghyavi lagte ka
[9:56 pm, 17/7/2026] Sakshi Kolekar Skn: Tuji sign lagel
[9:57 pm, 17/7/2026] Anushka Bhamare: Hod kinva dusrya konachi nahi na
[9:57 pm, 17/7/2026] Sakshi Kolekar Skn: Nahi
[9:58 pm, 17/7/2026] Anushka Bhamare: Ok
[9:59 pm, 17/7/2026] Anushka Bhamare: Aani Saturday la admission office chalu asnar ka
[10:34 pm, 17/7/2026] Sakshi Kolekar Skn: May be nahi
[10:36 pm, 17/7/2026] Anushka Bhamare: Hm
[10:36 pm, 17/7/2026] Anushka Bhamare: Old building la ghyaychay ka admission ka new building aani floor konta
[8:29 am, 18/7/2026] Sakshi Kolekar Skn: Old building admission office
'''
completion = client.chat.completions.create(
    model="gpt-4.1",
    messages=[
        {"role": "system",
            "content": "You are a person named harry who speaks hindi as well as english. He is from India and is a coder. You analyze chat history and respond like harry. ."},
        {"role": "user",
            "content": command}
    ]
)

print(completion.choices[0].message.content)