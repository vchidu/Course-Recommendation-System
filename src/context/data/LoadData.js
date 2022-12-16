import * as d3 from 'd3';
import data from './coursera.csv';


export const loadData = async()=> {
    return d3.csv(data)
};