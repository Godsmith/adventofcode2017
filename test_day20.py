from day20 import Particle, ParticleSwarm


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

    def test_moving_away_from_origin(self):
        particle = Particle.from_string('p=< 4,0,0>, v=<-1,0,0>, a=<0,0,0>')
        particle.tick()
        assert not particle.moving_away_from_origin


        particle = Particle.from_string('p=< 4,0,0>, v=<1,0,0>, a=<0,0,0>')
        particle.tick()
        particle.tick()
        print(particle._distance_last)
        print(particle._distance_before_last)
        assert particle.moving_away_from_origin

        particle = Particle.from_string('p=< 4,0,0>, v=<1,0,0>, a=<-1,0,0>')
        particle.tick()
        particle.tick()
        assert not particle.moving_away_from_origin


class TestParticleSwarm:
    def test_from_list(self):
        swarm = ParticleSwarm.from_strings(['p=< 3,2,-7>, v=< 2,0,0>, a=<-1,0,0>'])
        assert swarm._particles[0].velocity == [2, 0, 0]

    def test_index_closest_to_origin(self):
        swarm = ParticleSwarm.from_strings(['p=< 3,2,-7>, v=< 2,0,0>, a=<-1,0,0>',
                                            'p=< 2,2,-7>, v=< 2,0,0>, a=<-1,0,0>'])
        assert swarm.index_closest_to_origin == 1

    def test_all_moving_away_from_origin(self):
        swarm = ParticleSwarm.from_strings(['p=< 3,0,0>, v=< 2,0,0>, a=<-1,0,0>',
                                            'p=< 4,0,0>, v=< 0,0,0>, a=<-2,0,0>'])
        swarm.tick()
        swarm.tick()
        assert not swarm.all_moving_away_from_origin
        swarm.tick()
        swarm.tick()
        swarm.tick()
        assert swarm.all_moving_away_from_origin

    def test_index_closest_to_origin_long_term(self):
        swarm = ParticleSwarm.from_strings(['p=< 3,0,0>, v=< 2,0,0>, a=<-1,0,0>',
                                            'p=< 4,0,0>, v=< 0,0,0>, a=<-2,0,0>'])
        assert swarm.index_closest_to_origin_long_term() == 0
