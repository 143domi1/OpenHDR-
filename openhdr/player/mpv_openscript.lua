local utils = require 'mp.utils'
local msg = require 'mp.msg'
local json = require 'dkjson' -- You need to install dkjson.lua in same folder

local metadata
local current_scene = nil

function load_metadata()
    local path = mp.get_property("path")
    if not path then return end

    local base = utils.split_path(path)
    local name = utils.join_path(base, utils.get_filename(path))
    local meta_path = utils.join_path("metadata", name .. ".hdrmeta.json")

    local file = io.open(meta_path, "r")
    if not file then
        msg.warn("No HDR metadata found for", meta_path)
        return
    end

    local content = file:read("*all")
    file:close()
    metadata = json.decode(content)
end

function apply_scene(scene)
    if not scene then return end
    mp.set_property("video-params/brightness", tostring(scene.brightness or 1.0))
    mp.set_property("video-params/contrast", tostring(scene.contrast or 1.0))
    mp.set_property("video-params/saturation", tostring(scene.saturation or 1.0))
end

function on_tick()
    if not metadata or not metadata.scenes then return end
    local time = mp.get_property_number("time-pos")
    if not time then return end

    for _, scene in ipairs(metadata.scenes) do
        if time >= scene.start and time < scene.end then
            if current_scene ~= scene then
                current_scene = scene
                apply_scene(scene)
            end
            return
        end
    end
end

mp.register_event("file-loaded", load_metadata)
mp.add_periodic_timer(0.5, on_tick)
