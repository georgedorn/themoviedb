#!/usr/bin/env python3
#encoding:utf-8
#author:dbr/Ben
#project:themoviedb
#repository:http://github.com/dbr/tvdb_api
#license: LGPLv2 http://www.gnu.org/licenses/lgpl.html

import tmdb
import unittest

class tmdb_test(unittest.TestCase):
    def test_tmdb(self):
        m = tmdb.tmdb("Sin City")
        self.assertIsInstance(m,tmdb.tmdb)
    
    def test_tmdb_getTotal(self):
        m = tmdb.tmdb("Sin City")
        self.assertEqual(m.getTotal(),7)

    def test_browse(self):
        m = tmdb.Browse({"query":"Sin City"})
        self.assertIsInstance(m,tmdb.Browse)

    def test_browse_getTotal(self):
        m = tmdb.Browse({"query":"Sin City"})
        self.assertEqual(m.getTotal(),4)
    
    def test_imdb(self):
        m = tmdb.imdb(title="Sin City")
        self.assertIsInstance(m,tmdb.imdb)
    
    def test_imdb_getTotal(self):
        m = tmdb.imdb(title="Sin City")
        self.assertEqual(m.getTotal(),1)

if __name__ == '__main__':
    unittest.main()
