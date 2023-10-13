from mqt.ddsim.pathqasmsimulator import create_tensor_network
from qiskit import QuantumCircuit
from quimb.tensor import Circuit
import cotengra as ctg
import numpy as np
import random
from tddfork.TDD.TDD import Ini_TDD, TDD, cont
from tddfork.TDD.TN import Index,Tensor,TensorNetwork
from tddfork.TDD.TDD_Q import cir_2_tn,get_real_qubit_num,add_trace_line,add_inputs,add_outputs
import circuit_util as cu

def tn_to_tdd(tn: TensorNetwork):
    return tn.cont()

def circ_to_tdd(circuit: QuantumCircuit):
    tn, indices = cir_2_tn(circuit)
    Ini_TDD(index_order=indices)
    return tn.cont()

def tdd_contract(tdd1: TDD, tdd2: TDD):
    return cont(tdd1, tdd2)

def get_tdds_from_quimb_tensor_network(tensor_network):
    Ini_TDD(list(tensor_network.all_inds()))
    
    tdds = {}

    for i, tensor in tensor_network.tensor_map.items():
        t = Tensor(tensor.data, [Index(s) for s in tensor.inds])
        tdds[i] = t.tdd()

    return tdds