(ns qtools-clojure.algos.buy_signal1)
(use 'clojure.java.io)
(require '[clojure.string :as str])

(defn get-list [lines col]
	  (loop [x 0 list-vals []]
			(if (< x 10)
	  			(recur (inc x) (into list-vals (set [(nth (str/split (nth lines x) #",") 1)] )))
	  			(take-last (- (count list-vals) col) list-vals)))
	  
	)


(defn main []

;(with-open [rdr (reader "~/Quant/data/WIKI-DATA.csv")]
;  (doseq [line (line-seq rdr)]
 ;   (println line)))

	(with-open [rdr (reader "/home/lrrr/Quant/data/WIKI-AAPL.csv")]
		(def lines (line-seq rdr))
		(def open-vals (get-list lines 1))

	  )
	
	(println open-vals)
	)