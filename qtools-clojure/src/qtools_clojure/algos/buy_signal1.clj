(ns qtools-clojure.algos.buy_signal1)
(use 'clojure.java.io)
(require '[clojure.string :as str])

(defn get-list [lines col]
	(loop [x 0 list-vals []]
		(if (< x (count lines))
			(recur (inc x) (into list-vals (set [(nth (str/split (nth lines x) #",") col)] )))
			(take-last (- (count list-vals) col) list-vals)))

	)


(defn main []

	(with-open [rdr (reader "/home/lrrr/Quant/data/WIKI-AAPL.csv")]
		(def lines (line-seq rdr))
		(def open-vals (get-list lines 1 ))

	  )
	
	(println (count open-vals))
	)