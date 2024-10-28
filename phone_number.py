import phonenumbers
from phonenumbers import geocoder,carrier

phone_number= input("Enter your phone number with country code: ")

parsed_number=phonenumbers.parse(phone_number)

location = geocoder.description_for_number(parsed_number,'en')
service_provider=carrier.name_for_number(parsed_number,'en')

print(f"location : {location}")
print(f"carrier : {service_provider}")
 
