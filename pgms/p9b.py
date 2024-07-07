class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def addTime(self, other_time):
        total_minutes = (
            self.hours * 60 + self.minutes + other_time.hours * 60 + other_time.minutes
        )
        new_hours, new_minutes = divmod(total_minutes, 60)
        return Time(new_hours, new_minutes)

    def displayTime(self):
        print(f"{self.hours} hr {self.minutes} min")

    def displayMinutes(self):
        total_minutes = self.hours * 60 + self.minutes
        print(f"Total minutes: {total_minutes}")


# Example usage:
time1 = Time(2, 50)
time2 = Time(1, 20)

result = time1.addTime(time2)
result.displayTime()
result.displayMinutes()
