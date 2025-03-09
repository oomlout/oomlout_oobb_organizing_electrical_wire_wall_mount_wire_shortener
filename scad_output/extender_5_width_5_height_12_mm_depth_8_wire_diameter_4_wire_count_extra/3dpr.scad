$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, -6.0000000000]) {
			hull() {
				translate(v = [-32.0000000000, 32.0000000000, 0]) {
					cylinder(h = 12, r = 5);
				}
				translate(v = [32.0000000000, 32.0000000000, 0]) {
					cylinder(h = 12, r = 5);
				}
				translate(v = [-32.0000000000, -32.0000000000, 0]) {
					cylinder(h = 12, r = 5);
				}
				translate(v = [32.0000000000, -32.0000000000, 0]) {
					cylinder(h = 12, r = 5);
				}
			}
		}
	}
	union() {
		translate(v = [-22.5000000000, 30.0000000000, 0]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						#translate(v = [0, 0, -6.0000000000]) {
							cylinder(h = 6.0000000000, r = 1.5000000000);
						}
						#translate(v = [0, 0, -1.9000000000]) {
							cylinder(h = 1.9000000000, r1 = 1.8000000000, r2 = 3.6000000000);
						}
						#cylinder(h = 250, r = 3.6000000000);
						#translate(v = [0, 0, -6.0000000000]) {
							cylinder(h = 6.0000000000, r = 1.8000000000);
						}
						#translate(v = [0, 0, -6.0000000000]) {
							cylinder(h = 6.0000000000, r = 1.5000000000);
						}
					}
					union();
				}
			}
		}
		translate(v = [22.5000000000, -30.0000000000, 0]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						#translate(v = [0, 0, -6.0000000000]) {
							cylinder(h = 6.0000000000, r = 1.5000000000);
						}
						#translate(v = [0, 0, -1.9000000000]) {
							cylinder(h = 1.9000000000, r1 = 1.8000000000, r2 = 3.6000000000);
						}
						#cylinder(h = 250, r = 3.6000000000);
						#translate(v = [0, 0, -6.0000000000]) {
							cylinder(h = 6.0000000000, r = 1.8000000000);
						}
						#translate(v = [0, 0, -6.0000000000]) {
							cylinder(h = 6.0000000000, r = 1.5000000000);
						}
					}
					union();
				}
			}
		}
		translate(v = [22.5000000000, 30.0000000000, 0]) {
			rotate(a = [0, 0, 90]) {
				difference() {
					union() {
						#translate(v = [-1.7500000000, -3.2500000000, -0.3000000000]) {
							cube(size = [3.5000000000, 6.5000000000, 0.3000000000]);
						}
						#translate(v = [-1.7500000000, -1.7500000000, -0.6000000000]) {
							cube(size = [3.5000000000, 3.5000000000, 0.3000000000]);
						}
						#translate(v = [-1.7500000000, -3.2500000000, 2.5000000000]) {
							cube(size = [3.5000000000, 6.5000000000, 0.3000000000]);
						}
						#translate(v = [-1.7500000000, -1.7500000000, 2.8000000000]) {
							cube(size = [3.5000000000, 3.5000000000, 0.3000000000]);
						}
						#translate(v = [0, 0, -100.0000000000]) {
							cylinder(h = 200, r = 1.8000000000);
						}
						#translate(v = [-20.0000000000, -3.5053000000, 0]) {
							cube(size = [20, 7.0106000000, 2.6000000000]);
						}
						#linear_extrude(height = 2.6000000000) {
							polygon(points = [[3.5120000000, 0.0000000000], [1.7560000000, 3.0414812181], [-1.7560000000, 3.0414812181], [-3.5120000000, 0.0000000000], [-1.7560000000, -3.0414812181], [1.7560000000, -3.0414812181]]);
						}
						#translate(v = [-1.7500000000, -3.2500000000, -0.3000000000]) {
							cube(size = [3.5000000000, 6.5000000000, 0.3000000000]);
						}
						#translate(v = [-1.7500000000, -1.7500000000, -0.6000000000]) {
							cube(size = [3.5000000000, 3.5000000000, 0.3000000000]);
						}
						#translate(v = [-1.7500000000, -3.2500000000, 2.5000000000]) {
							cube(size = [3.5000000000, 6.5000000000, 0.3000000000]);
						}
						#translate(v = [-1.7500000000, -1.7500000000, 2.8000000000]) {
							cube(size = [3.5000000000, 3.5000000000, 0.3000000000]);
						}
						#translate(v = [0, 0, -100.0000000000]) {
							cylinder(h = 200, r = 1.8000000000);
						}
						#translate(v = [-1.7500000000, -3.2500000000, -0.3000000000]) {
							cube(size = [3.5000000000, 6.5000000000, 0.3000000000]);
						}
						#translate(v = [-1.7500000000, -1.7500000000, -0.6000000000]) {
							cube(size = [3.5000000000, 3.5000000000, 0.3000000000]);
						}
						#translate(v = [-1.7500000000, -3.2500000000, 2.5000000000]) {
							cube(size = [3.5000000000, 6.5000000000, 0.3000000000]);
						}
						#translate(v = [-1.7500000000, -1.7500000000, 2.8000000000]) {
							cube(size = [3.5000000000, 3.5000000000, 0.3000000000]);
						}
						#translate(v = [0, 0, -100.0000000000]) {
							cylinder(h = 200, r = 1.8000000000);
						}
					}
					union();
				}
			}
		}
		translate(v = [-22.5000000000, -30.0000000000, 0]) {
			rotate(a = [0, 0, 90]) {
				difference() {
					union() {
						#translate(v = [-1.7500000000, -3.2500000000, -0.3000000000]) {
							cube(size = [3.5000000000, 6.5000000000, 0.3000000000]);
						}
						#translate(v = [-1.7500000000, -1.7500000000, -0.6000000000]) {
							cube(size = [3.5000000000, 3.5000000000, 0.3000000000]);
						}
						#translate(v = [-1.7500000000, -3.2500000000, 2.5000000000]) {
							cube(size = [3.5000000000, 6.5000000000, 0.3000000000]);
						}
						#translate(v = [-1.7500000000, -1.7500000000, 2.8000000000]) {
							cube(size = [3.5000000000, 3.5000000000, 0.3000000000]);
						}
						#translate(v = [0, 0, -100.0000000000]) {
							cylinder(h = 200, r = 1.8000000000);
						}
						#translate(v = [0.0000000000, -3.5053000000, 0]) {
							cube(size = [20, 7.0106000000, 2.6000000000]);
						}
						#linear_extrude(height = 2.6000000000) {
							polygon(points = [[3.5120000000, 0.0000000000], [1.7560000000, 3.0414812181], [-1.7560000000, 3.0414812181], [-3.5120000000, 0.0000000000], [-1.7560000000, -3.0414812181], [1.7560000000, -3.0414812181]]);
						}
						#translate(v = [-1.7500000000, -3.2500000000, -0.3000000000]) {
							cube(size = [3.5000000000, 6.5000000000, 0.3000000000]);
						}
						#translate(v = [-1.7500000000, -1.7500000000, -0.6000000000]) {
							cube(size = [3.5000000000, 3.5000000000, 0.3000000000]);
						}
						#translate(v = [-1.7500000000, -3.2500000000, 2.5000000000]) {
							cube(size = [3.5000000000, 6.5000000000, 0.3000000000]);
						}
						#translate(v = [-1.7500000000, -1.7500000000, 2.8000000000]) {
							cube(size = [3.5000000000, 3.5000000000, 0.3000000000]);
						}
						#translate(v = [0, 0, -100.0000000000]) {
							cylinder(h = 200, r = 1.8000000000);
						}
						#translate(v = [-1.7500000000, -3.2500000000, -0.3000000000]) {
							cube(size = [3.5000000000, 6.5000000000, 0.3000000000]);
						}
						#translate(v = [-1.7500000000, -1.7500000000, -0.6000000000]) {
							cube(size = [3.5000000000, 3.5000000000, 0.3000000000]);
						}
						#translate(v = [-1.7500000000, -3.2500000000, 2.5000000000]) {
							cube(size = [3.5000000000, 6.5000000000, 0.3000000000]);
						}
						#translate(v = [-1.7500000000, -1.7500000000, 2.8000000000]) {
							cube(size = [3.5000000000, 3.5000000000, 0.3000000000]);
						}
						#translate(v = [0, 0, -100.0000000000]) {
							cylinder(h = 200, r = 1.8000000000);
						}
					}
					union();
				}
			}
		}
		translate(v = [7.5000000000, 30.0000000000, 6.0000000000]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, -12.0000000000]) {
							cylinder(h = 12, r = 2.0000000000);
						}
						translate(v = [0, 0, -3]) {
							cylinder(h = 3, r1 = 2.1250000000, r2 = 3.7500000000);
						}
						translate(v = [0, 0, -12.0000000000]) {
							cylinder(h = 12, r = 2.1250000000);
						}
						translate(v = [0, 0, -12.0000000000]) {
							cylinder(h = 12, r = 2.0000000000);
						}
					}
					union();
				}
			}
		}
		translate(v = [-7.5000000000, -30.0000000000, 6.0000000000]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, -12.0000000000]) {
							cylinder(h = 12, r = 2.0000000000);
						}
						translate(v = [0, 0, -3]) {
							cylinder(h = 3, r1 = 2.1250000000, r2 = 3.7500000000);
						}
						translate(v = [0, 0, -12.0000000000]) {
							cylinder(h = 12, r = 2.1250000000);
						}
						translate(v = [0, 0, -12.0000000000]) {
							cylinder(h = 12, r = 2.0000000000);
						}
					}
					union();
				}
			}
		}
		translate(v = [-7.5000000000, 30.0000000000, 6.0000000000]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, -12.0000000000]) {
							cylinder(h = 12, r = 2.0000000000);
						}
						translate(v = [0, 0, -3]) {
							cylinder(h = 3, r1 = 2.1250000000, r2 = 3.7500000000);
						}
						translate(v = [0, 0, -12.0000000000]) {
							cylinder(h = 12, r = 2.1250000000);
						}
						translate(v = [0, 0, -12.0000000000]) {
							cylinder(h = 12, r = 2.0000000000);
						}
					}
					union();
				}
			}
		}
		translate(v = [7.5000000000, -30.0000000000, 6.0000000000]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, -12.0000000000]) {
							cylinder(h = 12, r = 2.0000000000);
						}
						translate(v = [0, 0, -3]) {
							cylinder(h = 3, r1 = 2.1250000000, r2 = 3.7500000000);
						}
						translate(v = [0, 0, -12.0000000000]) {
							cylinder(h = 12, r = 2.1250000000);
						}
						translate(v = [0, 0, -12.0000000000]) {
							cylinder(h = 12, r = 2.0000000000);
						}
					}
					union();
				}
			}
		}
		translate(v = [-30.0000000000, 30.0000000000, -100.0000000000]) {
			cylinder(h = 200, r = 3.2500000000);
		}
		translate(v = [-15.0000000000, 30.0000000000, -100.0000000000]) {
			cylinder(h = 200, r = 3.2500000000);
		}
		translate(v = [0.0000000000, 30.0000000000, -100.0000000000]) {
			cylinder(h = 200, r = 3.2500000000);
		}
		translate(v = [15.0000000000, 30.0000000000, -100.0000000000]) {
			cylinder(h = 200, r = 3.2500000000);
		}
		translate(v = [30.0000000000, 30.0000000000, -100.0000000000]) {
			cylinder(h = 200, r = 3.2500000000);
		}
		translate(v = [-30.0000000000, -30.0000000000, -100.0000000000]) {
			cylinder(h = 200, r = 3.2500000000);
		}
		translate(v = [-15.0000000000, -30.0000000000, -100.0000000000]) {
			cylinder(h = 200, r = 3.2500000000);
		}
		translate(v = [0.0000000000, -30.0000000000, -100.0000000000]) {
			cylinder(h = 200, r = 3.2500000000);
		}
		translate(v = [15.0000000000, -30.0000000000, -100.0000000000]) {
			cylinder(h = 200, r = 3.2500000000);
		}
		translate(v = [30.0000000000, -30.0000000000, -100.0000000000]) {
			cylinder(h = 200, r = 3.2500000000);
		}
		translate(v = [-30.0000000000, 30.0000000000, -100.0000000000]) {
			cylinder(h = 200, r = 1.8000000000);
		}
		translate(v = [-22.5000000000, 30.0000000000, -100.0000000000]) {
			cylinder(h = 200, r = 1.8000000000);
		}
		translate(v = [-15.0000000000, 30.0000000000, -100.0000000000]) {
			cylinder(h = 200, r = 1.8000000000);
		}
		translate(v = [-7.5000000000, 30.0000000000, -100.0000000000]) {
			cylinder(h = 200, r = 1.8000000000);
		}
		translate(v = [0.0000000000, 30.0000000000, -100.0000000000]) {
			cylinder(h = 200, r = 1.8000000000);
		}
		translate(v = [7.5000000000, 30.0000000000, -100.0000000000]) {
			cylinder(h = 200, r = 1.8000000000);
		}
		translate(v = [15.0000000000, 30.0000000000, -100.0000000000]) {
			cylinder(h = 200, r = 1.8000000000);
		}
		translate(v = [22.5000000000, 30.0000000000, -100.0000000000]) {
			cylinder(h = 200, r = 1.8000000000);
		}
		translate(v = [30.0000000000, 30.0000000000, -100.0000000000]) {
			cylinder(h = 200, r = 1.8000000000);
		}
		translate(v = [-30.0000000000, -30.0000000000, -100.0000000000]) {
			cylinder(h = 200, r = 1.8000000000);
		}
		translate(v = [-22.5000000000, -30.0000000000, -100.0000000000]) {
			cylinder(h = 200, r = 1.8000000000);
		}
		translate(v = [-15.0000000000, -30.0000000000, -100.0000000000]) {
			cylinder(h = 200, r = 1.8000000000);
		}
		translate(v = [-7.5000000000, -30.0000000000, -100.0000000000]) {
			cylinder(h = 200, r = 1.8000000000);
		}
		translate(v = [0.0000000000, -30.0000000000, -100.0000000000]) {
			cylinder(h = 200, r = 1.8000000000);
		}
		translate(v = [7.5000000000, -30.0000000000, -100.0000000000]) {
			cylinder(h = 200, r = 1.8000000000);
		}
		translate(v = [15.0000000000, -30.0000000000, -100.0000000000]) {
			cylinder(h = 200, r = 1.8000000000);
		}
		translate(v = [22.5000000000, -30.0000000000, -100.0000000000]) {
			cylinder(h = 200, r = 1.8000000000);
		}
		translate(v = [30.0000000000, -30.0000000000, -100.0000000000]) {
			cylinder(h = 200, r = 1.8000000000);
		}
		translate(v = [-30.0000000000, 30.0000000000, -100.0000000000]) {
			cylinder(h = 200, r = 1.8000000000);
		}
		translate(v = [-22.5000000000, 30.0000000000, -100.0000000000]) {
			cylinder(h = 200, r = 1.8000000000);
		}
		translate(v = [-15.0000000000, 30.0000000000, -100.0000000000]) {
			cylinder(h = 200, r = 1.8000000000);
		}
		translate(v = [-7.5000000000, 30.0000000000, -100.0000000000]) {
			cylinder(h = 200, r = 1.8000000000);
		}
		translate(v = [0.0000000000, 30.0000000000, -100.0000000000]) {
			cylinder(h = 200, r = 1.8000000000);
		}
		translate(v = [7.5000000000, 30.0000000000, -100.0000000000]) {
			cylinder(h = 200, r = 1.8000000000);
		}
		translate(v = [15.0000000000, 30.0000000000, -100.0000000000]) {
			cylinder(h = 200, r = 1.8000000000);
		}
		translate(v = [22.5000000000, 30.0000000000, -100.0000000000]) {
			cylinder(h = 200, r = 1.8000000000);
		}
		translate(v = [30.0000000000, 30.0000000000, -100.0000000000]) {
			cylinder(h = 200, r = 1.8000000000);
		}
		translate(v = [-30.0000000000, -30.0000000000, -100.0000000000]) {
			cylinder(h = 200, r = 1.8000000000);
		}
		translate(v = [-22.5000000000, -30.0000000000, -100.0000000000]) {
			cylinder(h = 200, r = 1.8000000000);
		}
		translate(v = [-15.0000000000, -30.0000000000, -100.0000000000]) {
			cylinder(h = 200, r = 1.8000000000);
		}
		translate(v = [-7.5000000000, -30.0000000000, -100.0000000000]) {
			cylinder(h = 200, r = 1.8000000000);
		}
		translate(v = [0.0000000000, -30.0000000000, -100.0000000000]) {
			cylinder(h = 200, r = 1.8000000000);
		}
		translate(v = [7.5000000000, -30.0000000000, -100.0000000000]) {
			cylinder(h = 200, r = 1.8000000000);
		}
		translate(v = [15.0000000000, -30.0000000000, -100.0000000000]) {
			cylinder(h = 200, r = 1.8000000000);
		}
		translate(v = [22.5000000000, -30.0000000000, -100.0000000000]) {
			cylinder(h = 200, r = 1.8000000000);
		}
		translate(v = [30.0000000000, -30.0000000000, -100.0000000000]) {
			cylinder(h = 200, r = 1.8000000000);
		}
		translate(v = [-30.0000000000, 30.0000000000, -100.0000000000]) {
			cylinder(h = 200, r = 1.8000000000);
		}
		translate(v = [-22.5000000000, 30.0000000000, -100.0000000000]) {
			cylinder(h = 200, r = 1.8000000000);
		}
		translate(v = [-15.0000000000, 30.0000000000, -100.0000000000]) {
			cylinder(h = 200, r = 1.8000000000);
		}
		translate(v = [-7.5000000000, 30.0000000000, -100.0000000000]) {
			cylinder(h = 200, r = 1.8000000000);
		}
		translate(v = [0.0000000000, 30.0000000000, -100.0000000000]) {
			cylinder(h = 200, r = 1.8000000000);
		}
		translate(v = [7.5000000000, 30.0000000000, -100.0000000000]) {
			cylinder(h = 200, r = 1.8000000000);
		}
		translate(v = [15.0000000000, 30.0000000000, -100.0000000000]) {
			cylinder(h = 200, r = 1.8000000000);
		}
		translate(v = [22.5000000000, 30.0000000000, -100.0000000000]) {
			cylinder(h = 200, r = 1.8000000000);
		}
		translate(v = [30.0000000000, 30.0000000000, -100.0000000000]) {
			cylinder(h = 200, r = 1.8000000000);
		}
		translate(v = [-30.0000000000, -30.0000000000, -100.0000000000]) {
			cylinder(h = 200, r = 1.8000000000);
		}
		translate(v = [-22.5000000000, -30.0000000000, -100.0000000000]) {
			cylinder(h = 200, r = 1.8000000000);
		}
		translate(v = [-15.0000000000, -30.0000000000, -100.0000000000]) {
			cylinder(h = 200, r = 1.8000000000);
		}
		translate(v = [-7.5000000000, -30.0000000000, -100.0000000000]) {
			cylinder(h = 200, r = 1.8000000000);
		}
		translate(v = [0.0000000000, -30.0000000000, -100.0000000000]) {
			cylinder(h = 200, r = 1.8000000000);
		}
		translate(v = [7.5000000000, -30.0000000000, -100.0000000000]) {
			cylinder(h = 200, r = 1.8000000000);
		}
		translate(v = [15.0000000000, -30.0000000000, -100.0000000000]) {
			cylinder(h = 200, r = 1.8000000000);
		}
		translate(v = [22.5000000000, -30.0000000000, -100.0000000000]) {
			cylinder(h = 200, r = 1.8000000000);
		}
		translate(v = [30.0000000000, -30.0000000000, -100.0000000000]) {
			cylinder(h = 200, r = 1.8000000000);
		}
		translate(v = [22.5000000000, -22.5000000000, -6.0000000000]) {
			rotate(a = [0, 90, 0]) {
				cylinder(h = 15, r = 4.0000000000);
			}
		}
		translate(v = [-37.5000000000, -22.5000000000, -6.0000000000]) {
			rotate(a = [0, 90, 0]) {
				cylinder(h = 15, r = 4.0000000000);
			}
		}
		translate(v = [22.5000000000, -7.5000000000, -6.0000000000]) {
			rotate(a = [0, 90, 0]) {
				cylinder(h = 15, r = 4.0000000000);
			}
		}
		translate(v = [-37.5000000000, -7.5000000000, -6.0000000000]) {
			rotate(a = [0, 90, 0]) {
				cylinder(h = 15, r = 4.0000000000);
			}
		}
		translate(v = [22.5000000000, 7.5000000000, -6.0000000000]) {
			rotate(a = [0, 90, 0]) {
				cylinder(h = 15, r = 4.0000000000);
			}
		}
		translate(v = [-37.5000000000, 7.5000000000, -6.0000000000]) {
			rotate(a = [0, 90, 0]) {
				cylinder(h = 15, r = 4.0000000000);
			}
		}
		translate(v = [22.5000000000, 22.5000000000, -6.0000000000]) {
			rotate(a = [0, 90, 0]) {
				cylinder(h = 15, r = 4.0000000000);
			}
		}
		translate(v = [-37.5000000000, 22.5000000000, -6.0000000000]) {
			rotate(a = [0, 90, 0]) {
				cylinder(h = 15, r = 4.0000000000);
			}
		}
		translate(v = [0, 0, -6.0000000000]) {
			hull() {
				translate(v = [-28.2500000000, 20.7500000000, 0]) {
					cylinder(h = 12, r = 5);
				}
				translate(v = [28.2500000000, 20.7500000000, 0]) {
					cylinder(h = 12, r = 5);
				}
				translate(v = [-28.2500000000, -20.7500000000, 0]) {
					cylinder(h = 12, r = 5);
				}
				translate(v = [28.2500000000, -20.7500000000, 0]) {
					cylinder(h = 12, r = 5);
				}
			}
		}
	}
}