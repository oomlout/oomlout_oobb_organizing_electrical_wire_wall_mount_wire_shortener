$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, -12.5000000000]) {
			hull() {
				translate(v = [-32.0000000000, 32.0000000000, 0]) {
					cylinder(h = 25, r = 5);
				}
				translate(v = [32.0000000000, 32.0000000000, 0]) {
					cylinder(h = 25, r = 5);
				}
				translate(v = [-32.0000000000, -32.0000000000, 0]) {
					cylinder(h = 25, r = 5);
				}
				translate(v = [32.0000000000, -32.0000000000, 0]) {
					cylinder(h = 25, r = 5);
				}
			}
		}
	}
	union() {
		translate(v = [-22.5000000000, 30.0000000000, 0]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						#translate(v = [0, 0, -12.5000000000]) {
							cylinder(h = 12.5000000000, r = 1.5000000000);
						}
						#translate(v = [0, 0, -1.9000000000]) {
							cylinder(h = 1.9000000000, r1 = 1.8000000000, r2 = 3.6000000000);
						}
						#cylinder(h = 50, r = 3.6000000000);
						#translate(v = [0, 0, -12.5000000000]) {
							cylinder(h = 12.5000000000, r = 1.8000000000);
						}
						#translate(v = [0, 0, -12.5000000000]) {
							cylinder(h = 12.5000000000, r = 1.5000000000);
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
						#translate(v = [0, 0, -12.5000000000]) {
							cylinder(h = 12.5000000000, r = 1.5000000000);
						}
						#translate(v = [0, 0, -1.9000000000]) {
							cylinder(h = 1.9000000000, r1 = 1.8000000000, r2 = 3.6000000000);
						}
						#cylinder(h = 50, r = 3.6000000000);
						#translate(v = [0, 0, -12.5000000000]) {
							cylinder(h = 12.5000000000, r = 1.8000000000);
						}
						#translate(v = [0, 0, -12.5000000000]) {
							cylinder(h = 12.5000000000, r = 1.5000000000);
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
						#translate(v = [-20.0000000000, -3.6785000000, 0]) {
							cube(size = [20, 7.3570000000, 3.0000000000]);
						}
						#linear_extrude(height = 3.0000000000) {
							polygon(points = [[3.7120000000, 0.0000000000], [1.8560000000, 3.2146862988], [-1.8560000000, 3.2146862988], [-3.7120000000, 0.0000000000], [-1.8560000000, -3.2146862988], [1.8560000000, -3.2146862988]]);
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
						#translate(v = [0.0000000000, -3.6785000000, 0]) {
							cube(size = [20, 7.3570000000, 3.0000000000]);
						}
						#linear_extrude(height = 3.0000000000) {
							polygon(points = [[3.7120000000, 0.0000000000], [1.8560000000, 3.2146862988], [-1.8560000000, 3.2146862988], [-3.7120000000, 0.0000000000], [-1.8560000000, -3.2146862988], [1.8560000000, -3.2146862988]]);
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
		translate(v = [7.5000000000, 30.0000000000, 12.5000000000]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, -25.0000000000]) {
							cylinder(h = 25, r = 2.0000000000);
						}
						translate(v = [0, 0, -3.7000000000]) {
							cylinder(h = 3.7000000000, r1 = 2.1250000000, r2 = 4.3750000000);
						}
						translate(v = [0, 0, -25.0000000000]) {
							cylinder(h = 25, r = 2.1250000000);
						}
						translate(v = [0, 0, -25.0000000000]) {
							cylinder(h = 25, r = 2.0000000000);
						}
					}
					union();
				}
			}
		}
		translate(v = [-7.5000000000, -30.0000000000, 12.5000000000]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, -25.0000000000]) {
							cylinder(h = 25, r = 2.0000000000);
						}
						translate(v = [0, 0, -3.7000000000]) {
							cylinder(h = 3.7000000000, r1 = 2.1250000000, r2 = 4.3750000000);
						}
						translate(v = [0, 0, -25.0000000000]) {
							cylinder(h = 25, r = 2.1250000000);
						}
						translate(v = [0, 0, -25.0000000000]) {
							cylinder(h = 25, r = 2.0000000000);
						}
					}
					union();
				}
			}
		}
		translate(v = [-7.5000000000, 30.0000000000, 12.5000000000]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, -25.0000000000]) {
							cylinder(h = 25, r = 2.0000000000);
						}
						translate(v = [0, 0, -3.7000000000]) {
							cylinder(h = 3.7000000000, r1 = 2.1250000000, r2 = 4.3750000000);
						}
						translate(v = [0, 0, -25.0000000000]) {
							cylinder(h = 25, r = 2.1250000000);
						}
						translate(v = [0, 0, -25.0000000000]) {
							cylinder(h = 25, r = 2.0000000000);
						}
					}
					union();
				}
			}
		}
		translate(v = [7.5000000000, -30.0000000000, 12.5000000000]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, -25.0000000000]) {
							cylinder(h = 25, r = 2.0000000000);
						}
						translate(v = [0, 0, -3.7000000000]) {
							cylinder(h = 3.7000000000, r1 = 2.1250000000, r2 = 4.3750000000);
						}
						translate(v = [0, 0, -25.0000000000]) {
							cylinder(h = 25, r = 2.1250000000);
						}
						translate(v = [0, 0, -25.0000000000]) {
							cylinder(h = 25, r = 2.0000000000);
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
		translate(v = [22.5000000000, -22.5000000000, -12.5000000000]) {
			rotate(a = [0, 90, 0]) {
				cylinder(h = 15, r = 2.0000000000);
			}
		}
		translate(v = [-37.5000000000, -22.5000000000, -12.5000000000]) {
			rotate(a = [0, 90, 0]) {
				cylinder(h = 15, r = 2.0000000000);
			}
		}
		translate(v = [22.5000000000, -7.5000000000, -12.5000000000]) {
			rotate(a = [0, 90, 0]) {
				cylinder(h = 15, r = 2.0000000000);
			}
		}
		translate(v = [-37.5000000000, -7.5000000000, -12.5000000000]) {
			rotate(a = [0, 90, 0]) {
				cylinder(h = 15, r = 2.0000000000);
			}
		}
		translate(v = [22.5000000000, 7.5000000000, -12.5000000000]) {
			rotate(a = [0, 90, 0]) {
				cylinder(h = 15, r = 2.0000000000);
			}
		}
		translate(v = [-37.5000000000, 7.5000000000, -12.5000000000]) {
			rotate(a = [0, 90, 0]) {
				cylinder(h = 15, r = 2.0000000000);
			}
		}
		translate(v = [22.5000000000, 22.5000000000, -12.5000000000]) {
			rotate(a = [0, 90, 0]) {
				cylinder(h = 15, r = 2.0000000000);
			}
		}
		translate(v = [-37.5000000000, 22.5000000000, -12.5000000000]) {
			rotate(a = [0, 90, 0]) {
				cylinder(h = 15, r = 2.0000000000);
			}
		}
		translate(v = [0, 0, -12.5000000000]) {
			hull() {
				translate(v = [-28.2500000000, 20.7500000000, 0]) {
					cylinder(h = 25, r = 5);
				}
				translate(v = [28.2500000000, 20.7500000000, 0]) {
					cylinder(h = 25, r = 5);
				}
				translate(v = [-28.2500000000, -20.7500000000, 0]) {
					cylinder(h = 25, r = 5);
				}
				translate(v = [28.2500000000, -20.7500000000, 0]) {
					cylinder(h = 25, r = 5);
				}
			}
		}
	}
}