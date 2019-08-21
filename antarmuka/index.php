<?php 
require 'functions.php';

$lebah = query("SELECT * FROM koloni2");
$sensor = query("SELECT * FROM sensor ORDER BY id DESC LIMIT 1;");

$lebahMerahMasuk = query("SELECT * FROM koloni2 WHERE warna_lebah = 'merah' AND status = 'masuk'");
$lebahMerahKeluar = query("SELECT * FROM koloni2 WHERE warna_lebah = 'merah' AND status = 'keluar'");

$lebahHijauMasuk = query("SELECT * FROM koloni2 WHERE warna_lebah = 'hijau' AND status = 'masuk'");
$lebahHijauKeluar = query("SELECT * FROM koloni2 WHERE warna_lebah = 'hijau' AND status = 'keluar'");

$lebahBiruMasuk = query("SELECT * FROM koloni2 WHERE warna_lebah = 'biru' AND status = 'masuk'");
$lebahBiruKeluar = query("SELECT * FROM koloni2 WHERE warna_lebah = 'biru' AND status = 'keluar'");

$lebahKuningMasuk = query("SELECT * FROM koloni2 WHERE warna_lebah = 'kuning' AND status = 'masuk'");
$lebahKuningKeluar = query("SELECT * FROM koloni2 WHERE warna_lebah = 'kuning' AND status = 'keluar'");

// var_dump($sensor);
?>

<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>

    <link rel="stylesheet" href="assets/css/style.css">
    <link href="https://fonts.googleapis.com/css?family=Montserrat&display=swap" rel="stylesheet">

    <script src="https://kit.fontawesome.com/6f14ca3fd1.js"></script>
    
    <title>Dashboard - Bee Counter</title>
  </head>
  <body>
        <nav class="navbar navbar-custom fixed-top flex-md-nowrap p-0 shadow">
          <a class="navbar-brand col-sm-3 col-md-2 mr-0" href="#">Bee Counter</a>
          <ul class="navbar-nav px-3">
            <li class="nav-item text-nowrap">
              <a class="nav-link" href="#">Angga Nurhiman</a>
            </li>
          </ul>
        </nav>
        
        <div class="container-fluid">
          <div class="row">
            <nav class="col-md-2 d-none d-md-block sidebar">
              <div class="sidebar-sticky">
                <ul class="nav flex-column">
                  <li class="nav-item">
                    <a class="nav-link active" href="#">
                      <span data-feather="home"></span><i class="fas fa-home fa-lg"></i>Dashboard <span class="sr-only">(current)</span>
                    </a>
                  </li>
                  <!-- <li class="nav-item">
                    <a class="nav-link" href="#">
                      <span data-feather="file"></span><i class="fas fa-table fa-lg"></i>
                      Table
                    </a>
                  </li>                   -->
                </ul>               
              </div>
            </nav>
        
            <main role="main" class="col-md-9 ml-sm-auto col-lg-10 px-4 main">
              <div class="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom">
                <h1 class="h2">Dashboard</h1>
              </div>
        
              <!-- <canvas class="my-4 w-100" id="myChart" width="900" height="380"></canvas> -->
              <div class="container">
                <div class="row">

                  <!-- lebah warna merah -->
                  <div class="col-md-2 card">
                    <div class="row">
                      <div class="col-md-4">
                        <div id="kotak-merah"></div>
                      </div>
                      <div class="col-md-8">
                          <h6>Lebah Merah</h6>
                          <p>In : <?= count($lebahMerahMasuk)?> <br> Out : <?= count($lebahMerahKeluar)?></p>
                      </div>
                    </div>                
                  </div>
                  
                  <!-- lebah warna hijau -->
                  <div class="col-md-2 card">
                    <div class="row">
                      <div class="col-md-4">
                        <div id="kotak-hijau"></div>
                      </div>
                      <div class="col-md-8">
                          <h6>Lebah Hijau</h6>
                          <p>In : <?= count($lebahHijauMasuk)?> <br> Out : <?= count($lebahHijauKeluar)?></p>
                      </div>
                    </div>                
                  </div>

                  <!-- lebah warna biru -->
                  <div class="col-md-2 card">
                    <div class="row">
                      <div class="col-md-4">
                        <div id="kotak-biru"></div>
                      </div>
                      <div class="col-md-8">
                          <h6>Lebah Biru</h6>
                          <p>In : <?= count($lebahBiruMasuk)?> <br> Out : <?= count($lebahBiruKeluar)?></p>
                      </div>
                    </div>                
                  </div>

                  <!-- lebah warna kuning -->
                  <div class="col-md-2 card">
                    <div class="row">
                      <div class="col-md-4">
                        <div id="kotak-kuning"></div>
                      </div>
                      <div class="col-md-8">
                          <h6>Lebah Kuning</h6>
                          <p>In : <?= count($lebahKuningMasuk)?> <br> Out : <?= count($lebahKuningKeluar)?></p>
                      </div>
                    </div>                
                  </div>

                  <div class="col-md-2"></div>

                  <!-- sensor suhu -->
                  <div class="col-md-2 card-sensor">
                    <div class="row">
                      <div class="col-md-4">
                        <div class="icon-sensor"><i class="fas fa-temperature-low"></i></div>
                      </div>
                      <div class="col-md-8">
                          <h6>Suhu</h6>
                          <p><?= $sensor[0]["suhu"]; ?> &deg;C</p>
                      </div>
                    </div>                 
                  </div>
                  
                  <!-- sensor kelembaban -->
                  <div class="col-md-2 card-sensor">
                    <div class="row">
                      <div class="col-md-4">
                        <div class="icon-sensor"><i class="fas fa-tint"></i></div>
                      </div>
                      <div class="col-md-8">
                          <h6>Kelembaban</h6>
                          <p><?= $sensor[0]["kelembaban"]; ?>%</p>
                      </div>
                    </div>                
                  </div>

                  <!-- sensor intensitas cahaya -->
                  <div class="col-md-2 card-sensor">
                    <div class="row">
                      <div class="col-md-4">
                        <div class="icon-sensor"><i class="far fa-sun"></i></div>
                      </div>
                      <div class="col-md-8">
                          <h6>Intensitas Cahaya</h6>
                          <p><?= $sensor[0]["intensitas_cahaya"]; ?> Lux</p>
                      </div>
                    </div>                
                  </div>
                </div>
              </div>
              
              <div class="container tabel">
                <h5>Data Lebah Keluar/Masuk</h5>
                <div class="table-responsive">
                  <table class="table table-striped table-sm">
                    <thead>
                      <tr>
                        <th>No.</th>
                        <th>Warna Lebah</th>
                        <th>Status</th>
                        <th>Waktu</th>
                      </tr>
                    </thead>
                    <tbody>
                    <?php $i = 1; ?>
                    <?php foreach ($lebah as $row) :?>
                      <tr>
                        <td><?= $i++; ?></td>
                        <td><?= $row["warna_lebah"]; ?></td>
                        <td><?= $row["status"]; ?></td>
                        <td><?= $row["waktu"]; ?></td>
                      </tr>
                      <?php endforeach; ?>                
                    </tbody>
                  </table>
                </div>
              </div>
            </main>
          </div>
        </div>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
  </body>
</html>