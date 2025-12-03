
import { ref } from 'vue'
import type { Node, Edge } from '@vue-flow/core'


// Export nodes
export const nodes = ref<Node[]>([
    {
        id: "1",
        type: "decision",
        data: {
            a: "Farm",
            b: "Turbine",
            state: null,
            reachable: false
        },
        position: { x: 0, y: 0},
    },
    {
        id: "2",
        type: "decision",
        data: {
            a: "Dynamic",
            b: "Steady state",
            state: null,
            reachable: false
        },
        position: { x: 0, y: 0},
    },
    {
        id: "3",
        type: "decision",
        data: {
            a: "Power + Loads",
            b: "Power",
            state: null,
            reachable: false
        },
        position: { x: 0, y: 0},
    },
    {
        id: "4",
        type: "decision",
        data: {
            a: "Floating",
            b: "Land-based",
            state: null,
            reachable: false
        },
        position: { x: 0, y: 0},
    },
    {
        id: "5",
        type: "decision",
        data: {
            a: "ABL",
            b: "Synthetic Turbulence",
            state: null,
            reachable: false
        },
        position: { x: 0, y: 0},
    },
    {
        id: "6",
        type: "decision",
        data: {
            a: "Actuator methods",
            b: "Resolve geometry",
            state: null,
            reachable: false
        },
        position: { x: 0, y: 0},
    },
    {
        id: "7",
        type: "decision",
        data: {
            a: "Steady state",
            b: "Variable",
            state: null,
            reachable: false
        },
        position: { x: 0, y: 0},
    },
    {
        id: "8",
        type: "decision",
        data: {
            a: "Design / Batch",
            b: "Single Simulation",
            state: null,
            reachable: false
        },
        position: { x: 0, y: 0},
    },


    {
        id: "9",
        data: {
            label: "FLORIS (LF)",
            reachable: false
        },
        position: { x: 0, y: 0},
        type: "tool",
    },
    {
        id: "10",
        data: {
            label: "FAD (LF)",
            reachable: false
        },
        position: { x: 0, y: 0},
        type: "tool",
    },
    {
        id: "11",
        data: {
            label: "WindSE (MF)",
            reachable: false
        },
        position: { x: 0, y: 0},
        type: "tool",
    },
    {
        id: "12",
        data: {
            label: "FAST.Farm (MF)",
            reachable: false
        },
        position: { x: 0, y: 0},
        type: "tool",
    },
    {
        id: "13",
        data: {
            label: "ExaWind Stack (HF)",
            reachable: false
        },
        position: { x: 0, y: 0},
        type: "tool",
    },
    {
        id: "14",
        data: {
            label: "AMR-Wind (HF)",
            reachable: false
        },
        position: { x: 0, y: 0},
        type: "tool",
    },
    {
        id: "15",
        data: {
            label: "WISDEM (LF)",
            reachable: false
        },
        position: { x: 0, y: 0},
        type: "tool",
    },
    {
        id: "16",
        data: {
            label: "WEIS (MF)",
            reachable: false
        },
        position: { x: 0, y: 0},
        type: "tool",
    },
    {
        id: "17",
        data: {
            label: "OpenFAST (MF)",
            reachable: false
        },
        position: { x: 0, y: 0},
        type: "tool",
    },
    {
        id: "18",
        data: {
            label: "Ard (MF)",
            reachable: false
        },
        position: { x: 0, y: 0},
        type: "tool",
    },
    {
        id: "19",
        data: {
            label: "ERF (HF)",
            reachable: false
        },
        position: { x: 0, y: 0},
        type: "tool",
    },

]);

// Export edges
export const edges = ref<Edge[]>([
    { id: "e1-2", source: "1", target: "2", label: "a", type: "decisionEdge", data: { reachable: false } },
    { id: "e1-7", source: "1", target: "7", label: "b", type: "decisionEdge", data: { reachable: false } },
    { id: "e2-3", source: "2", target: "3", label: "a", type: "decisionEdge", data: { reachable: false } },
    { id: "e2-4", source: "2", target: "4", label: "b", type: "decisionEdge", data: { reachable: false } },
    { id: "e3-5", source: "3", target: "5", label: "a", type: "decisionEdge", data: { reachable: false } },
    { id: "e3-11", source: "3", target: "11", label: "b", type: "decisionEdge", data: { reachable: false } },
    { id: "e5-6", source: "5", target: "6", label: "a", type: "decisionEdge", data: { reachable: false } },
    { id: "e5-12", source: "5", target: "12", label: "b", type: "decisionEdge", data: { reachable: false } },
    { id: "e6-14", source: "6", target: "14", label: "a", type: "decisionEdge", data: { reachable: false } },
    { id: "e6-13", source: "6", target: "13", label: "b", type: "decisionEdge", data: { reachable: false } },
    { id: "e4-10", source: "4", target: "10", label: "a", type: "decisionEdge", data: { reachable: false } },
    { id: "e4-18a", source: "4", target: "18", label: "a", type: "decisionEdge", data: { reachable: false } },
    { id: "e4-9", source: "4", target: "9", label: "b", type: "decisionEdge", data: { reachable: false } },
    { id: "e4-18b", source: "4", target: "18", label: "b", type: "decisionEdge", data: { reachable: false } },
    { id: "e7-15", source: "7", target: "15", label: "a", type: "decisionEdge", data: { reachable: false } },
    { id: "e7-8", source: "7", target: "8", label: "b", type: "decisionEdge", data: { reachable: false } },
    { id: "e8-16", source: "8", target: "16", label: "a", type: "decisionEdge", data: { reachable: false } },
    { id: "e8-17", source: "8", target: "17", label: "b", type: "decisionEdge", data: { reachable: false } },
    { id: "e3-18", source: "3", target: "18", label: "b", type: "decisionEdge", data: { reachable: false } },
    { id: "e6-19", source: "6", target: "19", label: "a", type: "decisionEdge", data: { reachable: false } },
]);
