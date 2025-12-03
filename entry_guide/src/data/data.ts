
import { ref } from 'vue'
import type { Node, Edge } from '@vue-flow/core'


// Export nodes
export const nodes = ref<Node[]>([
    {
        id: "1",
        type: "decision",
        data: {
            a: "Measured data",
            b: "Simulation",
            state: null,
            reachable: false
        },
        position: { x: 0, y: 0},
    },
    {
        id: "2",
        type: "decision",
        data: {
            a: "Turbine Studies",
            b: "Wakes and Farm Control",
            state: null,
            reachable: false
        },
        position: { x: 0, y: 0},
    },
    {
        id: "3",
        type: "decision",
        data: {
            a: "Power Performance",
            b: "Loads",
            state: null,
            reachable: false
        },
        position: { x: 0, y: 0},
    },
    {
        id: "4",
        type: "decision",
        data: {
            a: "Visualization",
            b: "Analysis",
            state: null,
            reachable: false
        },
        position: { x: 0, y: 0},
    },
    {
        id: "5",
        type: "decision",
        data: {
            a: "Turbine",
            b: "Flowfield",
            state: null,
            reachable: false
        },
        position: { x: 0, y: 0},
    },
    {
        id: "6",
        type: "decision",
        data: {
            a: "Modal",
            b: "Time Series",
            state: null,
            reachable: false
        },
        position: { x: 0, y: 0},
    },


    {
        id: "7",
        data: {
            label: "FLASC (MF)",
            reachable: false
        },
        position: { x: 0, y: 0},
        type: "tool",
    },
    {
        id: "8",
        data: {
            label: "OpenOA (MF)",
            reachable: false
        },
        position: { x: 0, y: 0},
        type: "tool",
    },
    {
        id: "9",
        data: {
            label: "Other?",
            reachable: false
        },
        position: { x: 0, y: 0},
        type: "tool",
    },
    {
        id: "10",
        data: {
            label: "pCrunch (MF)",
            reachable: false
        },
        position: { x: 0, y: 0},
        type: "tool",
    },
    {
        id: "11",
        data: {
            label: "ACDC (MF)",
            reachable: false
        },
        position: { x: 0, y: 0},
        type: "tool",
    },
    {
        id: "12",
        data: {
            label: "pyDatView / WEIS (MF)",
            reachable: false
        },
        position: { x: 0, y: 0},
        type: "tool",
    },
    {
        id: "13",
        data: {
            label: "ParaView / VTK (MF)",
            reachable: false
        },
        position: { x: 0, y: 0},
        type: "tool",
    },

]);

// Export edges
export const edges = ref<Edge[]>([
    { id: "e1-2", source: "1", target: "2", label: "a", type: "decisionEdge", data: { reachable: false } },
    { id: "e1-4", source: "1", target: "4", label: "b", type: "decisionEdge", data: { reachable: false } },
    { id: "e2-3", source: "2", target: "3", label: "a", type: "decisionEdge", data: { reachable: false } },
    { id: "e2-7", source: "2", target: "7", label: "b", type: "decisionEdge", data: { reachable: false } },
    { id: "e3-8", source: "3", target: "8", label: "a", type: "decisionEdge", data: { reachable: false } },
    { id: "e3-9", source: "3", target: "9", label: "b", type: "decisionEdge", data: { reachable: false } },
    { id: "e4-5", source: "4", target: "5", label: "a", type: "decisionEdge", data: { reachable: false } },
    { id: "e4-10", source: "4", target: "10", label: "b", type: "decisionEdge", data: { reachable: false } },
    { id: "e5-6", source: "5", target: "6", label: "a", type: "decisionEdge", data: { reachable: false } },
    { id: "e6-11", source: "6", target: "11", label: "a", type: "decisionEdge", data: { reachable: false } },
    { id: "e6-12", source: "6", target: "12", label: "b", type: "decisionEdge", data: { reachable: false } },
    { id: "e5-13", source: "5", target: "13", label: "b", type: "decisionEdge", data: { reachable: false } },
]);
