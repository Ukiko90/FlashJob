<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Database Talenti - Platform</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-slate-50 text-slate-800 font-sans antialiased">

    <!-- Navbar Superiore -->
    <header class="bg-white border-b border-slate-200 sticky top-0 z-50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between h-16 items-center">
                <div class="flex items-center space-x-8">
                    <span class="font-bold text-xl text-indigo-600">Platform</span>
                    <nav class="hidden md:flex space-x-4">
                        <a href="#" class="text-slate-600 hover:text-indigo-600 px-3 py-2 rounded-md text-sm font-medium">Panoramica</a>
                        <a href="#" class="bg-indigo-50 text-indigo-700 px-3 py-2 rounded-md text-sm font-medium">Database Talenti</a>
                        <a href="#" class="text-slate-600 hover:text-indigo-600 px-3 py-2 rounded-md text-sm font-medium">Area Lavoratori</a>
                        <a href="#" class="text-slate-600 hover:text-indigo-600 px-3 py-2 rounded-md text-sm font-medium">Area Aziende</a>
                    </nav>
                </div>
                <div class="flex items-center space-x-4">
                    <span class="text-sm text-slate-500 bg-slate-100 px-3 py-1 rounded-full">Milano Hub • <strong>Online</strong></span>
                </div>
            </div>
        </div>
    </header>

    <!-- Contenuto Principale -->
    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        
        <!-- Intestazione Sezione -->
        <div class="mb-6">
            <h1 class="text-2xl font-bold text-slate-900">Database Talenti</h1>
            <p class="text-slate-500 text-sm mt-1">Esplora i professionisti disponibili e filtra per ruolo, zona o competenze.</p>
        </div>

        <!-- Barra di Ricerca e Filtri -->
        <div class="bg-white p-4 rounded-xl shadow-sm border border-slate-200 mb-8 grid grid-cols-1 md:grid-cols-3 gap-4">
            <div>
                <label for="search" class="block text-xs font-medium text-slate-500 mb-1">Cerca ruolo o competenza</label>
                <input type="text" id="search" placeholder="Es. Project Manager, Chef..." class="w-full px-3 py-2 border border-slate-300 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-indigo-500">
            </div>
            <div>
                <label for="zone" class="block text-xs font-medium text-slate-500 mb-1">Zona</label>
                <select id="zone" class="w-full px-3 py-2 border border-slate-300 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 bg-white">
                    <option>Tutte le zone</option>
                    <option>Milano Centro</option>
                    <option>Porta Romana</option>
                    <option>Brera / Duomo</option>
                </select>
            </div>
            <div>
                <label for="status" class="block text-xs font-medium text-slate-500 mb-1">Disponibilità</label>
                <select id="status" class="w-full px-3 py-2 border border-slate-300 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 bg-white">
                    <option>Tutti</option>
                    <option>Disponibile ora</option>
                    <option>Non disponibile</option>
                </select>
            </div>
        </div>

        <!-- Griglia dei Talenti -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            
            <!-- Card Talento 1: Marco Rossi -->
            <div class="bg-white rounded-xl shadow-sm border border-slate-200 p-6 flex flex-col justify-between relative hover:shadow-md transition-shadow">
                <div>
                    <div class="flex justify-between items-start mb-3">
                        <span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-emerald-50 text-emerald-700 border border-emerald-200">
                            🟢 Disponibile ora
                        </span>
                        <span class="text-xs font-bold bg-indigo-600 text-white px-2 py-0.5 rounded">TOP</span>
                    </div>
                    <h3 class="text-lg font-bold text-slate-900">Marco Rossi</h3>
                    <p class="text-xs text-slate-500 mt-1">Project Manager / Sala - Milano Centro</p>
                    
                    <div class="flex items-center mt-3 text-sm text-slate-600">
                        <span class="text-amber-500 font-bold mr-1">★ 4.9</span>
                        <span class="text-xs text-slate-400">(12 recensioni verificate)</span>
                    </div>
                </div>
                
                <div class="mt-6 pt-4 border-t border-slate-100 flex justify-between items-center">
                    <a href="#" class="text-indigo-600 hover:text-indigo-800 text-sm font-medium">Visualizza profilo</a>
                </div>
            </div>

            <!-- Card Talento 2: Davide Moretti -->
            <div class="bg-white rounded-xl shadow-sm border border-slate-200 p-6 flex flex-col justify-between relative hover:shadow-md transition-shadow">
                <div>
                    <div class="flex justify-between items-start mb-3">
                        <span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-emerald-50 text-emerald-700 border border-emerald-200">
                            🟢 Disponibile ora
                        </span>
                        <span class="text-xs font-bold bg-indigo-600 text-white px-2 py-0.5 rounded">TOP</span>
                    </div>
                    <h3 class="text-lg font-bold text-slate-900">Davide Moretti</h3>
                    <p class="text-xs text-slate-500 mt-1">Chef de Rang - Porta Romana</p>
                    
                    <div class="flex items-center mt-3 text-sm text-slate-600">
                        <span class="text-amber-500 font-bold mr-1">★ 4.8</span>
                        <span class="text-xs text-slate-400">(24 recensioni verificate)</span>
                    </div>
                </div>
                
                <div class="mt-6 pt-4 border-t border-slate-100 flex justify-between items-center">
                    <a href="#" class="text-indigo-600 hover:text-indigo-800 text-sm font-medium">Visualizza profilo</a>
                </div>
            </div>

            <!-- Card Talento 3: Sara Neri (Corretta dall'errore precedente) -->
            <div class="bg-white rounded-xl shadow-sm border border-slate-200 p-6 flex flex-col justify-between relative hover:shadow-md transition-shadow">
                <div>
                    <div class="flex justify-between items-start mb-3">
                        <span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-emerald-50 text-emerald-700 border border-emerald-200">
                            🟢 Disponibile ora
                        </span>
                    </div>
                    <h3 class="text-lg font-bold text-slate-900">Sara Neri</h3>
                    <p class="text-xs text-slate-500 mt-1">Event Manager - Brera / Duomo</p>
                    
                    <div class="flex items-center mt-3 text-sm text-slate-600">
                        <span class="text-amber-500 font-bold mr-1">★ 4.9</span>
                        <span class="text-xs text-slate-400">(15 recensioni verificate)</span>
                    </div>
                </div>
                
                <div class="mt-6 pt-4 border-t border-slate-100 flex justify-between items-center">
                    <a href="#" class="text-indigo-600 hover:text-indigo-800 text-sm font-medium">Visualizza profilo</a>
                </div>
            </div>

        </div>
    </main>

</body>
</html>