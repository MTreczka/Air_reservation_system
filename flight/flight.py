class Flight:
    def __init__(self, flight_number, plane):
        self.plane = plane
        self.flight_number = flight_number

        rows, letters = self.plane.get_seating_plan()

        self.seats = [None] + [{letter: None for letter in letters} for _ in rows]

    def get_airways(self):
        return self.flight_number[:2]

    def get_number(self):
        return self.flight_number[2:]

    def get_airplane_model(self):
        return self.plane.get_model()

    def _parse_seat(self, seat):
        rows, letters = self.plane.get_seating_plan()
        letter = seat[-1]

        if letter not in letters:
            raise ValueError(f'Invalid seat letter: {letter}')

        row_text = seat[:-1]

        try:
            row = int(row_text)
        except ValueError:
            raise ValueError(f'Invalid row digit: {row_text}')

        if row not in rows:
            raise ValueError(f'Row is out of airplane rows range: {row}')

        return row, letter

    def allocate_passenger(self, seat, passenger):
        row, letter = self._parse_seat(seat)

        if self.seats[row][letter] is not None:
            raise ValueError(f'Seat is already occupied: {seat}')

        self.seats[row][letter] = passenger

    def relocate_passenger(self, seat_from, seat_to):
        pass

    def get_num_empty_seats(self):
        counter = 0

        for row in self.seats:
            if row is not None:
                for passenger in row.values():
                    if passenger is None:
                        counter += 1

        return counter

    def get_num_empty_seats(self):
        return sum(sum(1 for passenger in row.values() if passenger is None) for row in self.seats if row is not None)
