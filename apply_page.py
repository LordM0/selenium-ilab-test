import random
from seleniumbase import BaseCase


class ApplyPage(BaseCase):
    careers_menu_item = 'menu-item-1373'
    country = "South Africa"
    job_listing = '/html/body/section/div[2]/div/div/div/div[3]/div[2]/div/div/div/div/div/div[1]/div[1]/div[2]/div[1]'
    apply_btn = '/html/body/section[2]/div[2]/div/div/div/div/div[2]/div[1]/a'
    applicant_name_field = 'applicant_name'
    applicant_name_input = "Some Name"
    applicant_email_field = 'email'
    applicant_email_input = "automationAssessment@iLABQuality.com"
    applicant_phone_field = 'phone'
    applicant_phone_input = str(0) + str(random.randint(10, 89)) + " " + str(random.randint(100, 999)) + " " + str(random.randint(1000, 9999))
    submit_btn = 'wpjb_submit'
    error_text = '/html/body/section[2]/div[2]/div/div/div/div/div[2]/div[2]/form/fieldset[1]/div[5]/div/ul'

    def load(self):
        # set driver link
        self.open('https://ilabquality.com')
        # selects careers
        self.click(self.careers_menu_item, "id")
        # selects South Africa
        self.click(self.country, "link text")
        # selects first job listing
        self.click(self.job_listing)
        # click Apply Online
        self.click(self.apply_btn)

    def enter_name(self):
        self.send_keys(self.applicant_name_field, self.applicant_name_input, "id")

    def enter_email(self):
        self.send_keys(self.applicant_email_field, self.applicant_email_input, "id")

    def random_phone(self):
        self.send_keys(self.applicant_phone_field, self.applicant_phone_input, "id")

    def submit(self):
        self.click(self.submit_btn, "id")
        # print error message
        print(self.get_text(self.error_text))
