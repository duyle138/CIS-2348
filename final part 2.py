#Duy Le 1913048
user_input = None
while user_input != 'q':
    user_input = input('Please enter an item with the manufacturer or item type or enter q to quit:')
    if user_input == 'q':
        break
    else:
        user_manufacturer = None
        user_type = None
        user_input = user_input.split()
        wrong_input = False
        for x in user_input:
            if x in manufacturer_types:
                if user_manufacturer:
                    wrong_input = True
                else:
                    user_manufacturer = x
            elif x in inv_types:
                if user_type:
                    wrong_input = True
                else:
                    user_type = x
        if not user_manufacturer or not user_type or wrong_input:
            print('No such item in inventory')
        else:
            keys = sorted(my_dict.keys(), key=lambda a: my_dict[a]['Item Price'],reverse=True)
            item_matches = []
            similar_items = {}
            for x in keys:
                if my_dict[x]['Item Type'] == user_type:
                    today = datetime.now().date()
                    service_date = my_dict[x]['Service Date']
                    service_expiration = datetime.strptime(service_date, '%m/%d/%y').date()
                    expired = service_expiration < today
                    if my_dict[x]['Manufacturer Name'] == user_manufacturer:
                        if not expired and not my_dict[x]['Item Damaged']:
                            item_matches.append((x, my_dict[x]))
                    else:
                        if not expired and not my_dict[x]['Item Damaged']:
                            similar_items[x] = my_dict[x]
            if item_matches:
                item = item_matches[0]
                item_id = item[0]
                manu_name = item[1]['Manufacturer Name']
                item_type = item[1]['Item Type']
                item_price = item[1]['Item Price']
                print('Your item is: {},{},{},{}'. format(item_id, manu_name, item_type, item_price))

                if similar_items:
                    price_match = item_price
                    closest_type = None
                    closest_price = None
                    for x in similar_items:
                        if closest_price is None:
                            closest_type = similar_items[x]
                            closest_price = abs(int(price_match) - int(similar_items[x]['Item Price']))
                            item_id = x
                            manu_name = similar_items[x]['Manufacturer Name']
                            item_type = similar_items[x]['Item Type']
                            item_price = similar_items[x]['Item Price']
                            continue
                        price_diff = abs(int(price_match) - int(similar_items[x]['Item Price']))
                        if price_diff < closest_price:
                            closest_type = x
                            closest_price = price_diff
                            item_id = x
                            manu_name = similar_items[x]['Manufacturer Name']
                            item_type = similar_items[x]['Item Type']
                            item_price = similar_items[x]['Item Price']
                    print('You may also consider: {},{},{},{}'.format(item_id, manu_name, item_type, item_price))
                else:
                    print('No such item in inventory')
