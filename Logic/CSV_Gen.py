import csv
import random
import math
from faker import Faker


fake = Faker()

TOTAL_RECORDS = 1000000
NOISE_PERCENTAGE = 0.05

num_noisy_records = math.ceil(TOTAL_RECORDS * NOISE_PERCENTAGE)

noisy_indices = set(random.sample(range(TOTAL_RECORDS), num_noisy_records))

print(f"Generating {TOTAL_RECORDS} records with {num_noisy_records} noisy rows...")

with open('Logic\Midterm\students.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['StudentID', 'StudentName', 'DayOfBirth', 'Math', 'CS', 'Eng'])
    
    for i in range(TOTAL_RECORDS):
        student_id = i + 1
        name = fake.name()
        dob = fake.date_of_birth(minimum_age=18, maximum_age=22).strftime('%Y-%m-%d')
        math_score = random.randint(0, 10)
        cs_score = random.randint(0, 10)
        eng_score = random.randint(0, 10)
        
        # Inject noise if the current index is in our pre-selected set
        if i in noisy_indices:
            noise_type = random.choice([
            'over_10_eng', 'over_10_math', 'over_10_cs',
            'null_cs', 'null_math', 'null_eng',
            'negative_math', 'negative_cs', 'negative_eng'
            ])
            if noise_type == 'negative_math':
             math_score = random.randint(-10, -1)
            elif noise_type == 'negative_cs':
             cs_score = random.randint(-10, -1)
            elif noise_type == 'negative_eng':
             eng_score = random.randint(-10, -1)
            elif noise_type == 'null_cs':
             cs_score = ''
            elif noise_type == 'null_math':
             math_score = ''
            elif noise_type == 'null_eng':
             eng_score = ''
            elif noise_type == 'over_10_eng':
             eng_score = random.randint(11, 20)
            elif noise_type == 'over_10_math':
             math_score = random.randint(11, 20)
            elif noise_type == 'over_10_cs':
             cs_score = random.randint(11, 20)
                
        writer.writerow([student_id, name, dob, math_score, cs_score, eng_score])