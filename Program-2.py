class TV:
    # Parent Class TV

    def __init__(self,brand,channel,price,inches,status,volume):
        # Initialize common attributes for all types of TVs
        self.brand = brand
        self.channel = channel
        self.price = price
        self.inches = inches
        self.status = status
        self.volume = volume
    
    def volume_control(self):
        # Method to control the volume of the TV
        user_vol = int(input("Enter the desired volume: "))
        if user_vol < 0:
            print("Volume cannot be below 0, Please choose another option greater than 0")
        elif user_vol > 100:
            print("Volume cannot be above 100, Please choose another option lesser than 100")
        elif user_vol >= 0 and user_vol <= 100:
            self.volume = user_vol
            print("Volume successfully changed to:",self.volume)

    def channel_control(self):
         # Method to control the channel of the TV
        user_channel = int(input("Enter the desired channel: "))
        if user_channel < 0:
            print("Channel cannot be below 0, Please choose another option greater than 0")
        elif user_channel > 50:
            print("Channel cannot be above 50, Resetting the channel back to current channel",self.channel)
        elif user_channel >= 0 and user_channel <= 50:
            self.channel = user_channel
            print("Channel successfully changed to:",self.channel)
    
    def reset_tv(self):
         # Method to reset the TV to default settings
        self.channel = 1
        self.volume = 50
        print("TV has been resetted with Volume as {}, Channel as {}".format(self.volume,self.channel))

    def tv_status(self):
        # Method to display the status of the TV
        print(self.brand, "TV at Channel", self.channel, "," "Volume", self.volume)

class LEDTV(TV):
    # Child Class LEDTV
    def __init__(self, brand, channel, price, inches, status, volume, 
                 screen_thickness, energy_usage, Lifespan, Refresh_Rate, viewingAngle, Backlight, Display_Details):
        # Initialize LED-specific attributes in addition to TV attributes
        super().__init__(brand, channel, price, inches, status, volume)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.Lifespan = Lifespan
        self.Refresh_Rate = Refresh_Rate
        self.viewingAngle = viewingAngle
        self.Backlight = Backlight
        self.Display_Details = Display_Details

class PlasmaTV(TV):
    # Child Class PlasmaTV
    def __init__(self, brand, channel, price, inches, status, volume, 
                 screen_thickness, energy_usage, Lifespan, Refresh_Rate, viewingAngle, Backlight, Display_Details):
        # Initialize Plasma-specific attributes in addition to TV attributes
        super().__init__(brand, channel, price, inches, status, volume)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.Lifespan = Lifespan
        self.Refresh_Rate = Refresh_Rate
        self.viewingAngle = viewingAngle
        self.Backlight = Backlight
        self.Display_Details = Display_Details

# Object Creation for LED TV Child class
Television = LEDTV("SONY",1, 50000.00 ,32,"ON",50, 6.1,"50W", "15 Years","120 Hz","60 deg","Edge Lit","LED")
# Method Calling for LED TV Child class
Television.volume_control()
Television.channel_control()
Television.tv_status()
Television.reset_tv()

# Object Creation for Plasma TV Child class
Television = PlasmaTV("Samsung",1, 43000.00 ,32,"ON", 50, 7.1,"70W", "10 Years","60 Hz","60 deg","Edge Lit","Plasma")
# Method Calling for Plasma TV Child class
Television.volume_control()
Television.channel_control()
Television.tv_status()
Television.reset_tv()