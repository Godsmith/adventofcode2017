from util import input_rows

class Particle:
    def __init__(self, position, velocity, acceleration):
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration
        self._distance = self._distance_from_origin(self.position)
        self._distance_last = self._distance
        self._distance_before_last = self._distance

    def __repr__(self):
        return f'Particle({self.position}, {self.velocity}, {self.acceleration})'

    @classmethod
    def from_string(cls, s):
        args = []
        for part in s.split('<')[1:]:
            comma_separated_string = part.split('>')[0]
            strings = comma_separated_string.split(',')
            args.append(list(map(int, strings)))
        return cls(*args)

    def tick(self):
        self._distance_before_last = self._distance_last
        self._distance_last = self._distance
        for i, _ in enumerate(self.position):
            self.velocity[i] += self.acceleration[i]
            self.position[i] += self.velocity[i]
        self._distance = self._distance_from_origin(self.position)

    @property
    def distance_from_origin(self):
        return self._distance

    @staticmethod
    def _distance_from_origin(position):
        return sum(map(abs, position))

    @property
    def moving_away_from_origin(self):
        most_recent_distance_delta = self._distance - self._distance_last
        previous_distance_delta = self._distance_last - self._distance_before_last
        return most_recent_distance_delta >= previous_distance_delta

class ParticleSwarm:
    def __init__(self, particles):
        self._particles = particles

    @classmethod
    def from_strings(cls, list_):
        particles = list(map(Particle.from_string, list_))
        return cls(particles)

    @property
    def index_closest_to_origin(self):
        distances = [p.distance_from_origin for p in self._particles]
        return distances.index(min(distances))

    def index_closest_to_origin_long_term(self):
        self.tick()
        self.tick()
        while not self.all_moving_away_from_origin:
            print('tick')
            self.tick()
        return self.index_closest_to_origin

    @property
    def all_moving_away_from_origin(self):
        return all((p.moving_away_from_origin for p in self._particles))

    def tick(self):
        for particle in self._particles:
            particle.tick()


if __name__ == '__main__':
    swarm = ParticleSwarm.from_strings(input_rows(20))
    print(swarm.index_closest_to_origin_long_term())

