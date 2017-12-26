from util import input_rows
from collections import defaultdict


class Particle:
    def __init__(self, position, velocity, acceleration):
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration

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
        for i, _ in enumerate(self.position):
            self.velocity[i] += self.acceleration[i]
            self.position[i] += self.velocity[i]

    @property
    def distance_from_origin(self):
        return sum(map(abs, self.position))

    @property
    def total_acceleration(self):
        return sum(map(abs, self.acceleration))

    @property
    def is_moving_away_from_origin(self):
        for i, coordinate in enumerate(self.position):
            if not self._has_same_sign(self.position[i], self.velocity[i],
                                       self.acceleration[i]):
                return False
        return True

    @staticmethod
    def _has_same_sign(*args):
        if all(map(lambda x: x >= 0, args)):
            return True
        if all(map(lambda x: x <= 0, args)):
            return True
        return False


class ParticleSwarm:
    def __init__(self, particles):
        self._particles = particles

    @classmethod
    def from_strings(cls, list_):
        particles = list(map(Particle.from_string, list_))
        return cls(particles)

    def index_closest_to_origin_long_term(self):
        return self._particles.index(
            self._particle_closest_to_origin_long_term())

    def _particle_closest_to_origin_long_term(self):
        while not self._all_moving_away_from_origin:
            self._tick()
        return list(self._particles_with_minimum_distance_to_origin(
            self._particles_with_minimum_acceleration()))[0]

    @property
    def _all_moving_away_from_origin(self):
        return all((p.is_moving_away_from_origin for p in self._particles))

    def _tick(self):
        for particle in self._particles:
            particle.tick()

    def _minimum_acceleration(self):
        return min(p.total_acceleration for p in self._particles)

    def _particles_with_minimum_acceleration(self):
        return set(p for p in self._particles if
                   p.total_acceleration == self._minimum_acceleration())

    @staticmethod
    def _minimum_distance_to_origin(particles):
        return min(p.distance_from_origin for p in particles)

    def _particles_with_minimum_distance_to_origin(self, particles):
        return set(p for p in self._particles if
                   p.distance_from_origin == self._minimum_distance_to_origin(
                       particles))


class CollidingSwarm(ParticleSwarm):
    def __init__(self, particles):
        super().__init__(particles)
        self._distances = self._create_distances()
        self._last_distances = None

    @property
    def count_after_collisions(self):
        while not self._scattering():
            self._tick()
            self._remove_colliding()
        return len(self._particles)

    def _remove_colliding(self):
        particles_from_position = defaultdict(set)
        for particle in self._particles:
            particles_from_position[tuple(particle.position)].add(particle)
        for _, particles in particles_from_position.items():
            if len(particles) > 1:
                for particle in particles:
                    self._remove_particle(particle)

    def _remove_particle(self, particle):
        index = self._particles.index(particle)
        del self._particles[index]
        del self._distances[index]
        del self._last_distances[index]

    def _create_distances(self):
        return [self._calculate_distances(particle) for i, particle in
                enumerate(self._particles)]

    def _calculate_distances(self, particle):
        return [self._distance(particle, other_particle) for other_particle in
                self._particles]

    def _scattering(self):
        if not self._last_distances:
            return False
        for i, _ in enumerate(self._particles):
            for current_distance, last_distance in zip(self._distances[i],
                                                       self._last_distances[i]):
                if current_distance < last_distance:
                    return False
        return True

    @staticmethod
    def _distance(particle1, particle2):
        return sum(abs(v1 - v2) for v1, v2 in
                   zip(particle1.position, particle2.position))

    def _tick(self):
        self._last_distances = self._distances
        super()._tick()
        self._distances = self._create_distances()


if __name__ == '__main__':
    swarm = ParticleSwarm.from_strings(input_rows(20))
    print(swarm.index_closest_to_origin_long_term())

    swarm = CollidingSwarm.from_strings(input_rows(20))
    print(swarm.count_after_collisions)
