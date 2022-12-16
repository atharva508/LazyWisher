# LazyWisher
A program that automatically generates a wish and sends it to your family members on either their personal numbers or the family group through whatsapp

1. download all the modules in a virtual environment to run the application.
2. The application assumes that you live in an Indian family, thus replicating the structure of wishes in the whatsapp groups.
3. Add the information of your family members in the csv file before running the application.
4. Add their personal numbers under the "ID" column to send them a wish in private messages or copy the group id and paste it under the column to send a wish on the family group.
Note( a. Add the phone number with the country code (i.e +91 for india etc)
      b. to retrive the group id copy the suffix of the group invite link)
5. The app can run continuously on your device, and it will check for events every 24 hours.
Note: The app only supports emojis on private messages due to the shortcomings of the underlying modules!
