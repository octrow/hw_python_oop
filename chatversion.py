class InfoMessage:
    """Training Information Message.

    Attributes:
        - workout_type (str): type of training ('running', 'walking', 'swimming')
        - duration (float): duration of the training, in minutes
        - distance (float): distance covered by the user, in kilometers
        - mean_speed (float): average speed over the distance, in km/h
        - calories (float): energy consumption in kilocalories
    """
    def __init__(self, workout_type: str, duration: float, distance: float, mean_speed: float, calories: float) -> None:
        self.workout_type = workout_type
        self.duration = duration
        self.distance = distance
        self.mean_speed = mean_speed
        self.calories = calories


class Training:
    """Training base class.

    Attributes:
        - action (int): action performed during the training, 1 for running, 2 for walking, 3 for swimming
        - duration (float): duration of the training, in minutes
        - weight (float): weight of the user, in kilograms

    """

    def __init__(self, action: int, duration: float, weight: float) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Get distance in km.

        Returns:
            float: distance covered during the training, in kilometers
        """
        pass

    def get_mean_speed(self) -> float:
        """Get average driving speed.

        Returns:
            float: average speed during the training, in km/h
        """
        pass

    def get_spent_calories(self) -> float:
        """Get the number of calories expended.

        Returns:
            float: energy consumption during the training, in kilocalories
        """
        pass

    def show_training_info(self) -> InfoMessage:
        """Return an information message about the workout performed.

        Returns:
            InfoMessage: message containing information about the training
        """
        pass


class Running(Training):
    """Training: running.

    Attributes:
        - action (int): action performed during the training, 1 for running
        - duration (float): duration of the training, in minutes
        - weight (float): weight of the user, in kilograms
        - step_frequency (float): average number of steps per minute
    """
    def __init__(self, duration: float, weight: float, step_frequency: float) -> None:
        super().__init__(1, duration, weight)
        self.step_frequency = step_frequency

    def get_distance(self) -> float:
        """Get distance in km.

        Returns:
            float: distance covered during the running training, in kilometers
        """
        return self.step_frequency * self.duration / 60000

    def get_mean_speed(self) -> float:
        """Get average driving speed.

        Returns:
            float: average speed during the running training, in km/h
        """
        return self.get_distance() / (self.duration / 3600)

###############
############
###############

class SportsWalking(Training):
    """Training: sportswalking.

    Attributes:
        - action (int): action performed during the training, 2 for walking
        - duration (float): duration of the training, in minutes
        - weight (float): weight of the user, in kilograms
        - step_frequency (float): average number of steps per minute
    """
    def __init__(self, duration: float, weight: float, step_frequency: float) -> None:
        super().__init__(2, duration, weight)
        self.step_frequency = step_frequency

    def get_distance(self) -> float:
        """Get distance in km.

        Returns:
            float: distance covered during the sports walking training, in kilometers
        """
        return self.step_frequency * self.duration / 60000

    def get_mean_speed(self) -> float:
        """Get average driving speed.

        Returns:
            float: average speed during the sports walking training, in km/h
        """
        return self.get_distance() / (self.duration / 3600)


class Swimming(Training):
    """Training: swimming.

    Attributes:
        - action (int): action performed during the training, 3 for swimming
        - duration (float): duration of the training, in minutes
        - weight (float): weight of the user, in kilograms
        - pool_length (float): length of the pool, in meters
        - strokes_per_minute (float): average number of strokes per minute
    """
    def __init__(self, duration: float, weight: float, pool_length: float, strokes_per_minute: float) -> None:
        super().__init__(3, duration, weight)
        self.pool_length = pool_length
        self.strokes_per_minute = strokes_per_minute

    def get_distance(self) -> float:
        """Get distance in km.

        Returns:
            float: distance covered during the swimming training, in kilometers
        """
        return self.pool_length * self.strokes_per_minute * self.duration / 60000

    def get_mean_speed(self) -> float:
        """Get average driving speed.

        Returns:
            float: average speed during the swimming training, in km/h
        """
        return self.get_distance() / (self.duration / 3600)


def read_package(workout_type: str, data: list) -> Training:
    """Read data received from sensors.

    Args:
        workout_type (str): type of training, 'SWM' for swimming, 'RUN' for running, 'WLK' for sports walking
        data (list): data received from the sensors

    Returns:
        Training: training object with the data from the sensors
    """
    if workout_type == 'SWM':
        return Swimming(*data)
    elif workout_type == 'RUN':
        return Running(*data)
    elif workout_type == 'WLK':
        return SportsWalking(*data)


def main(training: Training) -> None:
    """main function.

    Args:
        training (Training): training object with the data from the sensors
    """
    distance = training.get_distance()
    mean_speed = training.get_mean_speed()
    calories = training.get_spent_calories()

    message = InfoMessage(training.workout_type, training.duration, distance, mean_speed, calories)
    print(message)
