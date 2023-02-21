import sys
sys.path.append('./')

from AsymmetryFactor.particle.particle_class import ParticleAttributes

from AsymmetryFactor.beams.beam_class import BeamAttributes
from AsymmetryFactor.beams.gaussian.gaussian_class import GaussAttributes
from AsymmetryFactor.beams.bessel.bessel_class import BesselAttributes
from AsymmetryFactor.beams.frozenwave.frozenwave_class import FrozenWaveAttributes
from AsymmetryFactor.j1 import j1

from simulations.create_graph import plot_graphic

import numpy as np
import csv
import json
import math
import sys


def create_particles(data_particles):
    # qnt_particles = len(data_particles)
    # print(f'receive {qnt_particles} particles')

    matrix = False
    list_of_particles = []

    for particle in data_particles:
        m = complex(particle["m"])
        # print(f'type of m is: {type(m)}, and your value {m}')
        ur = particle["ur"]
        # print(f'type of ur is: {type(ur)}')

        x = particle["x"]
        # print(x)

        if isinstance(x, dict):
            # print(f'type of x is: {type(x)}')
            # print(x)
            begin_value = x["begin"]
            end_value = x["end"]
            qnt_x = x["qnt_points"]
            # print(begin_value)
            # print(end_value)
            # print(qnt_x)

            x_values = np.linspace(begin_value, end_value, qnt_x)
            particle = []
            # aux=0
            for x_i in x_values:
                # print(f'point: {x_i}')
                particle.append(ParticleAttributes(x_i, m, ur))

            list_of_particles.append(particle)

        else:
            list_of_particles.append(ParticleAttributes(x, m, ur))

    # print(list_of_particles)
    if isinstance(list_of_particles[0], list):
        # for i in list_of_particles:
        #     for j in i:
        #         j.print_particle_attributes()
        matrix = True

    # else:
        # for i in list_of_particles:
        #     i.print_particle_attributes()

    return list_of_particles, matrix
        


def create_beams(data_beam):
    # print(data_beam)
    # print(f'receive {len(data_beam)} beams')

    matrix = False
    list_of_beams = []

    for beam in data_beam:
        type_beam = beam["type"]

        if type_beam == "PW":
            # print("Is Plane Wave")
            list_of_beams.append(BeamAttributes())
            # return BeamAttributes(), matrix
        
        elif type_beam == "FW":
            # print("Is Frozen Wave")

            var_lambda = beam["var_lambda"]
            var_lambda = eval(var_lambda)

            k = beam["k"]
            k = eval(k)
            # print(k)

            # nano = 10**(-9)
            # var_lambda = 1064 * (10**(-9))
            # k = (2*math.pi) / var_lambda
            # print(k)

            q = beam["q"]
            q = eval(q)
            # print(q)
            # q = 0.8*k
            # print(q)

            l = beam["l"]

            n = beam["n"]

            z0 = beam["z0"]

            if isinstance(z0, dict):
                begin = z0["begin"]
                if isinstance(z0, str):
                    begin = eval(begin)
                
                end = z0["end"]
                if isinstance(end, str):
                    end = eval(end)

                qnt_z0 = z0["qnt_points"]
                
                beams = []

                z0_values = np.linspace(begin, end, qnt_z0)
                for i_z0 in z0_values:
                    beams.append(FrozenWaveAttributes(k, i_z0, q, l, n))

                list_of_beams.append(beams)

            else:
                list_of_beams.append(FrozenWaveAttributes(k, z0, q, l, n))


        elif type_beam == "GB":
            ...

        elif type_beam == "BB":
            ...

        if any(type(i) is list for i in list_of_beams):
            # print("is a list of list")
            # for i in list_of_beams:
            #     for j in i:
            #         j.print_beam_attributes()
            matrix = True

        # else:
        #     # print("is just a list")
        #     for i in list_of_beams:
        #         i.print_beam_attributes()

        return list_of_beams, matrix


def matrix_beam_matrix_particle(beams, particle, writer_csv):
    print("matrix_beam_matrix_particle")

def matrix_beam_list_particle(beams, particle, writer_csv): 
    print("matrix_beam_list_particle")

    for i_p in particle:    
        row = []
        # result_i_p = []
        print("**********************************")
        i_p.print_particle_attributes()
        row.append(i_p.particle_info())
        row.append(beams[0].beam_info())
        
        for j_b in beams:
            j_b.print_beam_attributes()
            row.append(j1(i_p, j_b)) # pass operation graph or time
        
        print(row)
        writer_csv.writerow(row)

def list_beam_matrix_particle(beams, particle, writer_csv):
    print("list_beam_matrix_particle")

    for i_b in beams:    
        row = []
        i_b.print_beam_attributes()
        print("**********************************")
        row.append(i_b.beam_info())
        row.append(particle[0].particle_info())
        
        for j_p in particle:
            j_p.print_particle_attributes()

            row.append(j1(j_p, i_b)) 
        
        print(row)
        writer_csv.writerow(row)

def list_beam_list_particle(beams, particle):
    print("list_beam_list_particle")


if __name__ == "__main__":
    print(f"Arguments count: {len(sys.argv)-1}")

    for i, arg in enumerate(sys.argv):
        if i == 0:
            continue
        print(f"Argument {i}: {arg}")
        
        with open(arg, "r") as read_json_file:
            data = json.load(read_json_file)
            
            print(data["name"])

            # if data["graph"] != None:
            #     graph_file_name = "./simulations/outputs/graph_result/"+data["name"] + ".csv"
            #     graph_file = open(graph_file_name, 'w', newline='')
            #     writer_csv_file = csv.writer(graph_file)

            particles, m_particles = create_particles(data["particle"])
            beams, m_beams = create_beams(data["beam"])

            if m_beams and m_particles:
                matrix_beam_matrix_particle(beams, particles)
            
            elif m_beams == True and m_particles == False:
                print("matrix_beam_list_particle")
                # for i_b in beams:
                #     matrix_beam_list_particle(i_b, particles, writer_csv_file)

                # graph_file.close()

            elif m_beams == False and m_particles == True:
                print("list_beam_matrix_particle")
                # for i_p in particles:
                #     list_beam_matrix_particle(beams, i_p, writer_csv_file)
                
                # graph_file.close()
            
            elif (not m_beams) and (not m_particles):
                list_beam_list_particle(beams, particles)



            