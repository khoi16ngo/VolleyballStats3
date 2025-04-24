<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Livewire Counter</title>
    @vite('resources/css/app.css')
    @livewireStyles
</head>
<body class="flex items-center justify-center h-screen bg-gray-100">
    <div class="bg-blue-500 text-white p-10">
        Tailwind is working!
    </div>

    <livewire:counter />

    @livewireScripts
</body>
</html>
