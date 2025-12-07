package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
)

var grid [][]string
var ans int
var dirs = [][]int{
	{0,1},
	{1,0},
	{0,-1},
	{-1,0},
	{1,1},
	{-1,-1},
	{1,-1},
	{-1,1},
}

func inbound(x int, y int) bool{
	return x >= 0 && x < len(grid) && y>= 0 && y < len(grid[0])
}

func solve([][]string) {
	for i := range len(grid){
		for j:= range len(grid[0]) {
			count := 0
			if grid[i][j] == "."{
				continue
			}

			for _, val := range dirs{
				x,y := val[0],val[1]
				nx, ny := x + i, y + j
				if !inbound(nx,ny){
					continue
				}
				if grid[nx][ny] == "@"{
					count += 1
				}
			}

			if count < 4{
				ans += 1
			}
		}
	}
}

func main(){
	filePath := "input.txt"
	file, err := os.Open(filePath)
	if err != nil {
		log.Fatalf("file not found")
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		row := strings.Split(line, "")
		grid =  append(grid, row)
	}
	solve(grid)
	fmt.Println(ans)
}