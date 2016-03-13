(ns qtools-clojure.algos.buy_signal1)
(use 'clojure.java.io)
(require '[clojure.string :as str])

(defn get-list [lines col]
	(loop [x 0 list-vals []]
		(if (< x (count lines))
			(recur (inc x) (into list-vals (set [(nth (str/split (nth lines x) #",") col)] )))
			(subvec list-vals 1 (count lines))))
	)

(defn calculate-slope [list-vals sample-size]
	(loop [x 1 x-loop-vec []]
		(if (< x (+ sample-size 1))
			(recur (inc x) (into x-loop-vec (set [x])))
			(def x-vals x-loop-vec)
			))
	(def y-vals (map read-string list-vals))
	(/ (- (* sample-size (reduce + (map * x-vals y-vals)) (* (reduce + x-vals) (reduce + y-vals))))
		(- (* sample-size (reduce + (map * x-vals x-vals))) (* (reduce + x-vals) (reduce + x-vals))))
		
	)

(defn main []

	(with-open [rdr (reader "/home/lrrr/Quant/data/WIKI-AAPL.csv")]
		(def lines (line-seq rdr))
		;(def open-vals (get-list lines 1 ))
		;(def high-vals (get-list lines 2 ))
		;(def low-vals (get-list lines 3 ))
		(def close-vals (get-list lines 4 ))
		;(def vol-vals (get-list lines 5 ))
	  )
	(def x 0)
	(def sample-size 5)
	(println (calculate-slope (subvec close-vals x (+ x sample-size)) sample-size))
	)