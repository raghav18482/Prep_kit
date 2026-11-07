from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from itertools import count


class VehicleType(Enum):
    BIKE = "bike"
    CAR = "car"


@dataclass(frozen=True)
class Vehicle:
    plate: str
    kind: VehicleType


@dataclass
class ParkingSpot:
    number: int
    kind: VehicleType
    vehicle: Vehicle | None = None

    @property
    def available(self) -> bool: return self.vehicle is None

    def park(self, vehicle: Vehicle) -> None:
        if not self.available or self.kind != vehicle.kind:
            raise ValueError("spot unavailable or incompatible")
        self.vehicle = vehicle

    def leave(self) -> Vehicle:
        if self.vehicle is None: raise ValueError("spot is empty")
        vehicle, self.vehicle = self.vehicle, None
        return vehicle


@dataclass(frozen=True)
class Ticket:
    id: int
    spot_number: int


class ParkingLot:
    def __init__(self, spots: list[ParkingSpot]) -> None:
        self.spots = {spot.number: spot for spot in spots}
        self.tickets: dict[int, Ticket] = {}
        self._ids = count(1)

    def park(self, vehicle: Vehicle) -> Ticket:
        spot = next((s for s in self.spots.values() if s.available and s.kind == vehicle.kind), None)
        if spot is None: raise ValueError("no spot available")
        spot.park(vehicle)
        ticket = Ticket(next(self._ids), spot.number)
        self.tickets[ticket.id] = ticket
        return ticket

    def unpark(self, ticket_id: int) -> Vehicle:
        ticket = self.tickets.pop(ticket_id)
        return self.spots[ticket.spot_number].leave()


if __name__ == "__main__":
    lot = ParkingLot([ParkingSpot(1, VehicleType.CAR), ParkingSpot(2, VehicleType.BIKE)])
    ticket = lot.park(Vehicle("KA01AB1234", VehicleType.CAR))
    print(ticket, lot.unpark(ticket.id))
