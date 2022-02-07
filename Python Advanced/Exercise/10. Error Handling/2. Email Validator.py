from errors import NameTooShortError, MustContainAtSymbolError, InvalidDomainError

domains = ["com", "bg", "org", "net"]

while True:
    line = input()
    if line == "End":
        break

    email_parts = line.split("@")

    if len(email_parts) == 1:
        raise MustContainAtSymbolError("Email must contain @")

    name, domain_name_domain = email_parts

    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    domain = domain_name_domain.split(".")[-1]

    if domain not in domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")