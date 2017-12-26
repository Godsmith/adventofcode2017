from day20 import Particle, ParticleSwarm, CollidingSwarm


class TestParticle:
    def test_from_string(self):
        particle = Particle.from_string('p=< 3,0,0>, v=< 2,0,0>, a=<-1,0,0>')
        assert particle.position == [3, 0, 0]
        assert particle.velocity == [2, 0, 0]
        assert particle.acceleration == [-1, 0, 0]

    def test_tick(self):
        particle = Particle.from_string('p=< 3,0,0>, v=< 2,0,0>, a=<-1,0,0>')
        particle.tick()
        assert particle.position == [4, 0, 0]
        assert particle.velocity == [1, 0, 0]
        assert particle.acceleration == [-1, 0, 0]

    def test_distance_from_origin(self):
        particle = Particle.from_string('p=< 3,2,-7>, v=< 2,0,0>, a=<-1,0,0>')
        assert particle.distance_from_origin == 12

    def test_acceleration_from_origin(self):
        particle = Particle.from_string('p=< 3,2,-7>, v=< 2,0,0>, a=<-1,2,0>')
        assert particle.total_acceleration == 3

    def test_has_same_sign(self):
        assert Particle._has_same_sign(1, 0, 2)
        assert Particle._has_same_sign(-1, 0, -2)
        assert not Particle._has_same_sign(1, 0, -2)

    def test_moving_away_from_origin(self):
        particle = Particle.from_string('p=< 4,0,0>, v=<-1,0,0>, a=<0,0,0>')
        assert not particle.is_moving_away_from_origin

        particle = Particle.from_string('p=< 4,0,0>, v=<1,0,0>, a=<0,0,0>')
        assert particle.is_moving_away_from_origin


class TestParticleSwarm:
    def test_from_list(self):
        swarm = ParticleSwarm.from_strings(
            ['p=< 3,2,-7>, v=< 2,0,0>, a=<-1,0,0>'])
        assert swarm._particles[0].velocity == [2, 0, 0]

    def test_all_moving_away_from_origin(self):
        swarm = ParticleSwarm.from_strings(
            ['p=< 3,0,0>, v=< 2,0,0>, a=<-1,0,0>',
             'p=< 4,0,0>, v=< 0,0,0>, a=<-2,0,0>'])
        swarm._tick()
        swarm._tick()
        assert not swarm._all_moving_away_from_origin
        swarm._tick()
        swarm._tick()
        swarm._tick()
        assert swarm._all_moving_away_from_origin

    def test_index_closest_to_origin_long_term(self):
        swarm = ParticleSwarm.from_strings(
            ['p=< 3,0,0>, v=< 2,0,0>, a=<-1,0,0>',
             'p=< 4,0,0>, v=< 0,0,0>, a=<-2,0,0>'])
        assert swarm.index_closest_to_origin_long_term() == 0


class TestCollidingSwarm:
    particle_strings = """p=<-6,0,0>, v=< 3,0,0>, a=< 0,0,0>
        p=<-4,0,0>, v=< 2,0,0>, a=< 0,0,0>
        p=<-2,0,0>, v=< 1,0,0>, a=< 0,0,0>
        p=< 3,0,0>, v=<-1,0,0>, a=< 0,0,0>""".split('\n')

    def test_remove_colliding(self):
        swarm = CollidingSwarm.from_strings(self.particle_strings)
        swarm._tick()
        swarm._tick()
        swarm._remove_colliding()
        assert len(swarm._particles) == 1

    def test_count_after_collisions(self):
        swarm = CollidingSwarm.from_strings(self.particle_strings)
        assert swarm.count_after_collisions == 1
