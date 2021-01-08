MyultimateSkills = {
    "Network": {
        "CCNA" : "100%",
        "CCNP" : "80%",
        "ENCOR" : "60%"
    },
    "Programming" : {
        "Python" : "30%",
        "HTML" : "70%"
    }
}
for main_key, main_value in MyultimateSkills.items():
    print (f"Diaa's Skills in a {main_key} is :- ")
    for child_key, child_value in main_value.items():
        print(f"- {child_key} ==>  {child_value} .")
