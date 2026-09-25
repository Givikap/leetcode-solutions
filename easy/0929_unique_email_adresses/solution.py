class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        unique_emails = set()

        for email in emails:
            name, domain = email.split("@")

            name = name.replace(".", "")

            skip_loc = name.find("+")
            if skip_loc != -1:
                name = name[:skip_loc]

            unique_emails.add(f"{name}@{domain}")

        return len(unique_emails)
