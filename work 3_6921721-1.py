# available cars and their costs(in usd) in the shop
cars={"toyota":50000,"kia":30000,"chevrolet":10000,"honda":6000,
      "ford":55000,"mercedesBenz":88000,"jeep":90000,"BMW":45000,"porshe":40000,"subaru":100000,"GMU":65700,"jaguar":56390,"ferrari":185260,
     "volvo":38465,"acura":53640,"bentley":6542800,"dodge":26473,"lincoln":3245670,"hyundai":4326,"landRover":43950,"tesla":788860,"chrysler":45000,
     "infiniti":665500,"maserati":245600,"mitsubushi":4545500,"bugatti":7000000,"mini":32200,"genesis":67500,"peugeot":3200,"renault":43900,
     "hudson":9000,"MG":55500,"daewoo":800900,"citroen":670000,"suzuki":45000,"pontiac":88900,"madz":7700,"cadillac":655000,}
car_name=input("do you have enter a car_name:")
if car_name in cars:
    print("yes,we have")
#if car is present,
    car_cost=cars[car_name]
    print(f"the cost of {car_name} is ${car_cost}.")
else:
#if car_name is absent,
     print("oops,your preferred car is not availabe.")

    


      